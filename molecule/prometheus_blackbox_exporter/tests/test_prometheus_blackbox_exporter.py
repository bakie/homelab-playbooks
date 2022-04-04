import pytest
import yaml

PROMETHEUS_BLACKBOX_EXPORTER_USER = "prometheus_blackbox_exporter"
PROMETHEUS_BLACKBOX_EXPORTER_GROUP = "prometheus_blackbox_exporter"
PROMETHEUS_BLACKBOX_EXPORTER_PATH = "/opt/prometheus/blackbox_exporter"
PROMETHEUS_BLACKBOX_EXPORTER_BASE_PATH = "/opt/prometheus"
PROMETHEUS_BLACKBOX_EXPORTER_CONFIG_PATH = "/etc/prometheus/blackbox_exporter"
PROMETHEUS_BLACKBOX_EXPORTER_BASE_CONFIG_PATH = "/etc/prometheus"


@pytest.fixture()
def ansible_defaults():
    with open("roles/prometheus_blackbox_exporter/vars/main.yml", 'r') as stream:
        return yaml.full_load(stream)


@pytest.mark.parametrize("path, owner", [
    (PROMETHEUS_BLACKBOX_EXPORTER_PATH, PROMETHEUS_BLACKBOX_EXPORTER_USER),
    (PROMETHEUS_BLACKBOX_EXPORTER_BASE_PATH, "root"),
    (PROMETHEUS_BLACKBOX_EXPORTER_CONFIG_PATH, PROMETHEUS_BLACKBOX_EXPORTER_USER),
    (PROMETHEUS_BLACKBOX_EXPORTER_BASE_CONFIG_PATH, "root")
])
def test_directory_owner(host, path, owner):
    assert host.file(path).user == owner


@pytest.mark.parametrize("path, group", [
    (PROMETHEUS_BLACKBOX_EXPORTER_PATH, PROMETHEUS_BLACKBOX_EXPORTER_GROUP),
    (PROMETHEUS_BLACKBOX_EXPORTER_BASE_PATH, "root"),
    (PROMETHEUS_BLACKBOX_EXPORTER_CONFIG_PATH, PROMETHEUS_BLACKBOX_EXPORTER_GROUP),
    (PROMETHEUS_BLACKBOX_EXPORTER_BASE_CONFIG_PATH, "root")
])
def test_directory_group(host, path, group):
    assert host.file(path).group == group


@pytest.mark.parametrize("path", [
    PROMETHEUS_BLACKBOX_EXPORTER_PATH,
    PROMETHEUS_BLACKBOX_EXPORTER_BASE_PATH,
    PROMETHEUS_BLACKBOX_EXPORTER_CONFIG_PATH,
    PROMETHEUS_BLACKBOX_EXPORTER_BASE_CONFIG_PATH
])
def test_directory_permissions(host, path):
    assert host.file(path).mode == 0o755


@pytest.mark.parametrize("file", [
    PROMETHEUS_BLACKBOX_EXPORTER_PATH + "/blackbox_exporter",
    PROMETHEUS_BLACKBOX_EXPORTER_CONFIG_PATH + "/config.yml",
    "/etc/systemd/system/prometheus_blackbox_exporter.service",
])
def test_files(host, file):
    assert host.file(file).is_file


def test_prometheus_blackbox_exporter_service_is_running(host):
    assert host.service("prometheus_blackbox_exporter").is_running


def test_prometheus_blackbox_exporter_service_is_enabled(host):
    assert host.service("prometheus_blackbox_exporter").is_enabled


def test_listening_on_port(host):
    assert host.socket("tcp://0.0.0.0:9103").is_listening


def test_capabilities(host):
    assert "blackbox_exporter = cap_net_raw+ep" in host.run("getcap " + PROMETHEUS_BLACKBOX_EXPORTER_PATH + "/blackbox_exporter").stdout


def test_version(host, ansible_defaults):
    version = ansible_defaults['prometheus_blackbox_exporter_version']
    assert (host.run(PROMETHEUS_BLACKBOX_EXPORTER_PATH+"/blackbox_exporter --version 2>&1 | head -1 | awk '{print $3}' | xargs echo -n").stdout == version)
