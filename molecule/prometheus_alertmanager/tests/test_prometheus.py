import pytest
import yaml


PROMETHEUS_ALERTMANAGER_USER = "prometheus_alertmanager"
PROMETHEUS_ALERTMANAGER_GROUP = "prometheus_alertmanager"
PROMETHEUS_ALERTMANAGER_PATH = "/opt/prometheus/alertmanager"
PROMETHEUS_ALERTMANAGER_BASE_PATH = "/opt/prometheus"
PROMETHEUS_ALERTMANAGER_CONFIG_PATH = "/etc/prometheus/alertmanager"
PROMETHEUS_ALERTMANAGER_BASE_CONFIG_PATH = "/etc/prometheus"
PROMETHEUS_ALERTMANAGER_DATA_PATH = "/opt/prometheus/alertmanager_data"
PROMETHEUS_ALERTMANAGER_AMTOOL_CONFIG_PATH = "/etc/amtool"


@pytest.fixture()
def ansible_defaults():
    with open("roles/prometheus_alertmanager/vars/main.yml", 'r') as stream:
        return yaml.full_load(stream)


def test_user_is_in_prometheus_alertmanager_group(host):
    assert PROMETHEUS_ALERTMANAGER_GROUP in host.user(PROMETHEUS_ALERTMANAGER_USER).groups


@pytest.mark.parametrize("path, owner", [
    (PROMETHEUS_ALERTMANAGER_PATH, PROMETHEUS_ALERTMANAGER_USER),
    (PROMETHEUS_ALERTMANAGER_BASE_PATH, "root"),
    (PROMETHEUS_ALERTMANAGER_CONFIG_PATH, PROMETHEUS_ALERTMANAGER_USER),
    (PROMETHEUS_ALERTMANAGER_BASE_CONFIG_PATH, "root"),
    (PROMETHEUS_ALERTMANAGER_DATA_PATH, PROMETHEUS_ALERTMANAGER_USER)
])
def test_directory_owner(host, path, owner):
    assert host.file(path).user == owner


@pytest.mark.parametrize("path, group", [
    (PROMETHEUS_ALERTMANAGER_PATH, PROMETHEUS_ALERTMANAGER_GROUP),
    (PROMETHEUS_ALERTMANAGER_BASE_PATH, "root"),
    (PROMETHEUS_ALERTMANAGER_CONFIG_PATH, PROMETHEUS_ALERTMANAGER_GROUP),
    (PROMETHEUS_ALERTMANAGER_BASE_CONFIG_PATH, "root"),
    (PROMETHEUS_ALERTMANAGER_DATA_PATH, PROMETHEUS_ALERTMANAGER_GROUP)
])
def test_directory_group(host, path, group):
    assert host.file(path).group == group


@pytest.mark.parametrize("path", [
    PROMETHEUS_ALERTMANAGER_PATH,
    PROMETHEUS_ALERTMANAGER_BASE_PATH,
    PROMETHEUS_ALERTMANAGER_CONFIG_PATH,
    PROMETHEUS_ALERTMANAGER_BASE_CONFIG_PATH,
    PROMETHEUS_ALERTMANAGER_DATA_PATH
])
def test_directory_permissions(host, path):
    assert host.file(path).mode == 0o755


def test_amtool_config_file_path(host):
    assert host.file(PROMETHEUS_ALERTMANAGER_AMTOOL_CONFIG_PATH+"/config.yml").contains("alertmanager.url: http://127.0.0.1:9093")


def test_version(host, ansible_defaults):
    version = ansible_defaults['prometheus_alertmanager_version']
    assert (host.run(PROMETHEUS_ALERTMANAGER_PATH+"/alertmanager --version 2>&1 | head -1 | awk '{print $3}' | xargs echo -n").stdout == version)


def test_prometheus_alertmanager_service_is_running(host):
    assert host.service("prometheus_alertmanager").is_running


def test_prometheus_alertmanager_service_is_enabled(host):
    assert host.service("prometheus_alertmanager").is_enabled


def test_listening_on_port(host):
    assert host.socket("tcp://0.0.0.0:9093").is_listening
