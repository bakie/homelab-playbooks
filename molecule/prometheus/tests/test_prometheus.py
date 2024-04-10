import pytest
import yaml


PROMETHEUS_USER = "prometheus"
PROMETHEUS_GROUP = "prometheus"
PROMETHEUS_PATH = "/opt/prometheus/prometheus"
PROMETHEUS_BASE_PATH = "/opt/prometheus"
PROMETHEUS_CONFIG_PATH = "/etc/prometheus/prometheus"
PROMETHEUS_RULES_CONFIG_PATH = "/etc/prometheus/prometheus/rules"
PROMETHEUS_FILE_SD_CONFIG_PATH = "/etc/prometheus/prometheus/file_sd"
PROMETHEUS_BASE_CONFIG_PATH = "/etc/prometheus"
PROMETHEUS_DATA_PATH = "/opt/prometheus/prometheus_data"


@pytest.fixture()
def ansible_defaults():
    with open("roles/prometheus/vars/main.yml", 'r') as stream:
        return yaml.full_load(stream)


def test_user_is_in_prometheus_group(host):
    assert PROMETHEUS_GROUP in host.user(PROMETHEUS_USER).groups


@pytest.mark.parametrize("path, owner", [
    (PROMETHEUS_PATH, PROMETHEUS_USER),
    (PROMETHEUS_BASE_PATH, "root"),
    (PROMETHEUS_CONFIG_PATH, PROMETHEUS_USER),
    (PROMETHEUS_BASE_CONFIG_PATH, "root"),
    (PROMETHEUS_DATA_PATH, PROMETHEUS_USER),
    (PROMETHEUS_RULES_CONFIG_PATH, PROMETHEUS_USER),
    (PROMETHEUS_FILE_SD_CONFIG_PATH, PROMETHEUS_USER)
])
def test_directory_owner(host, path, owner):
    assert host.file(path).user == owner


@pytest.mark.parametrize("path, group", [
    (PROMETHEUS_PATH, PROMETHEUS_GROUP),
    (PROMETHEUS_BASE_PATH, "root"),
    (PROMETHEUS_CONFIG_PATH, PROMETHEUS_GROUP),
    (PROMETHEUS_BASE_CONFIG_PATH, "root"),
    (PROMETHEUS_DATA_PATH, PROMETHEUS_GROUP),
    (PROMETHEUS_RULES_CONFIG_PATH, PROMETHEUS_GROUP),
    (PROMETHEUS_FILE_SD_CONFIG_PATH, PROMETHEUS_GROUP)
])
def test_directory_group(host, path, group):
    assert host.file(path).group == group


@pytest.mark.parametrize("path", [
    PROMETHEUS_PATH,
    PROMETHEUS_BASE_PATH,
    PROMETHEUS_CONFIG_PATH,
    PROMETHEUS_BASE_CONFIG_PATH,
    PROMETHEUS_DATA_PATH,
    PROMETHEUS_RULES_CONFIG_PATH,
    PROMETHEUS_FILE_SD_CONFIG_PATH
])
def test_directory_permissions(host, path):
    assert host.file(path).mode == 0o755


def test_blackbox_exporter_targets_json_file_sd_exists(host):
    assert host.file(PROMETHEUS_FILE_SD_CONFIG_PATH+"/blackbox_exporter_targets.json").exists


@pytest.mark.parametrize("setting", [
    "blackbox_green.com",
    "green",
    "blackbox_green",
    "blackbox_blue.com",
    "blue",
    "blackbox_blue"
])
def test_blackbox_exporter_targets_json_file_sd(host, setting):
    assert host.file(PROMETHEUS_FILE_SD_CONFIG_PATH+"/blackbox_exporter_targets.json").contains(setting)


@pytest.mark.parametrize("config", [
    "rule_files:",
    "alerting",
    PROMETHEUS_FILE_SD_CONFIG_PATH+"/blackbox_exporter_targets.json"
])
def test_prometheus_config(host, config):
    assert host.file(PROMETHEUS_CONFIG_PATH+"/prometheus.yml").contains(config)


def test_rules(host):
    assert host.file(PROMETHEUS_RULES_CONFIG_PATH+"/prometheus_monitoring.yml").exists


def test_prometheus_correct_version_is_installed(host, ansible_defaults):
    version = ansible_defaults['prometheus_version']
    assert (host.run(PROMETHEUS_PATH+"/prometheus --version 2>&1 | head -1 | awk '{print $3}' | xargs echo -n").stdout == version)


def test_prometheus_service_is_running(host):
    assert host.service('prometheus').is_running


def test_prometheus_service_is_enabled(host):
    assert host.service('prometheus').is_enabled


def test_listening_on_port(host):
    assert host.socket("tcp://127.0.0.1:9090").is_listening


def test_hosts_file(host):
    assert host.file("/etc/hosts").contains("ubuntu-focal-prometheus")
