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


def test_service(host):
    assert host.service("prometheus").is_running


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


@pytest.mark.parametrize(("group_name", "alert_rule", "alert_expr"), [
    ("group1", "single_rule", "up == 0"),
    ("group2", "rule one", "up == 0"),
    ("group2", "rule two", "up == 0")
])
def test_alerting_rules(host, group_name, alert_rule, alert_expr):
    assert host.file(PROMETHEUS_CONFIG_PATH + "/rules/alerting_rules.yml").contains(group_name)
    assert host.file(PROMETHEUS_CONFIG_PATH + "/rules/alerting_rules.yml").contains(alert_rule)
    assert host.file(PROMETHEUS_CONFIG_PATH + "/rules/alerting_rules.yml").contains(alert_expr)
