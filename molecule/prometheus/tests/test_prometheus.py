import pytest
import yaml

PROMETHEUS_HOME = "/opt/prometheus"
PROMETHEUS_CONFIG_PATH = "/etc/prometheus"


@pytest.fixture()
def ansible_defaults():
    with open("roles/prometheus/vars/main.yml", 'r') as stream:
        return yaml.full_load(stream)


@pytest.mark.parametrize("dir", [
    PROMETHEUS_CONFIG_PATH + "/rules",
    PROMETHEUS_CONFIG_PATH + "/file_sd",
    PROMETHEUS_CONFIG_PATH + "/conf.d"
])
def test_directories(host, dir):
    d = host.file(dir)
    assert d.is_directory
    assert d.exists


@pytest.mark.parametrize("file", [
    PROMETHEUS_CONFIG_PATH + "/prometheus.yml",
    PROMETHEUS_HOME + "/prometheus",
    PROMETHEUS_HOME + "/promtool",
    "/lib/systemd/system/prometheus.service",
])
def test_files(host, file):
    f = host.file(file)
    assert f.exists
    assert f.is_file


def test_user(host):
    assert host.group("prometheus").exists
    assert host.user("prometheus").exists


def test_prometheus_is_running(host):
    assert host.service("prometheus").is_running


def test_prometheus_is_enabled(host):
    assert host.service("prometheus").is_enabled


def test_socket(host):
    assert host.socket("tcp://0.0.0.0:9090").is_listening


def test_version(host, ansible_defaults):
    version = ansible_defaults['prometheus_version']
    out = host.run(PROMETHEUS_HOME + "/prometheus --version").stdout
    assert "prometheus, version " + version in out


@pytest.mark.parametrize(("target_url", "target_label"), [
    ("blackbox_green.com", "blackbox_green"),
    ("blackbox_blue.com", "blackbox_blue"),
])
def test_blackbox_targets(host, target_url, target_label):
    assert host.file(PROMETHEUS_CONFIG_PATH + "/file_sd/blackbox_targets.json").contains(target_url)
    assert host.file(PROMETHEUS_CONFIG_PATH + "/file_sd/blackbox_targets.json").contains(target_label)


@pytest.mark.parametrize("setting", [
    "alerting",
    "- targets: \\['localhost:9093'\\]"
])
def test_prometheus_config_file(host, setting):
    assert host.file(PROMETHEUS_CONFIG_PATH + "/prometheus.yml").contains(setting)


def test_rules(host):
    assert host.file(PROMETHEUS_CONFIG_PATH+"/rules/prometheus_monitoring.yml").exists