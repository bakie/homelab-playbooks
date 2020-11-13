import pytest
import yaml

prometheus_home = "/opt/prometheus"
prometheus_config_path = "/etc/prometheus"


@pytest.fixture()
def ansible_defaults():
    with open("../../defaults/main.yml", 'r') as stream:
        return yaml.load(stream)


@pytest.mark.parametrize("dir", [
    prometheus_config_path + "/rules",
    prometheus_config_path + "/file_sd",
    prometheus_config_path + "/conf.d"
])
def test_directories(host, dir):
    d = host.file(dir)
    assert d.is_directory
    assert d.exists


@pytest.mark.parametrize("file", [
    prometheus_config_path + "/prometheus.yml",
    prometheus_home + "/prometheus",
    prometheus_home + "/promtool",
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
    s = host.socket("tcp://0.0.0.0:9090")
    assert s.is_listening


def test_version(host, ansible_defaults):
    version = ansible_defaults['prometheus_version']
    out = host.run(prometheus_home + "/prometheus --version").stderr
    assert "prometheus, version " + version in out


def test_apache_vhost_sites_available(host):
    assert host.file("/etc/apache2/sites-available/prometheus.conf").exists


def test_apache_vhost_sites_enabled(host):
    assert host.file("/etc/apache2/sites-enabled/prometheus.conf").is_symlink


@pytest.mark.parametrize(("target_url", "target_label"), [
    ("blackbox_green.com", "blackbox_green"),
    ("blackbox_blue.com", "blackbox_blue"),
])
def test_blackbox_targets(host, target_url, target_label):
    assert host.file(prometheus_config_path + "/file_sd/blackbox_targets.json").contains(target_url)
    assert host.file(prometheus_config_path + "/file_sd/blackbox_targets.json").contains(target_label)


@pytest.mark.parametrize(("group_name", "alert_rule", "alert_expr"), [
    ("group1", "single_rule", "up == 0"),
    ("group2", "rule one", "up == 0"),
    ("group2", "rule two", "up == 0")
])
def test_alerting_rules(host, group_name, alert_rule, alert_expr):
    assert host.file(prometheus_config_path + "/rules/alerting_rules.yml").contains(group_name)
    assert host.file(prometheus_config_path + "/rules/alerting_rules.yml").contains(alert_rule)
    assert host.file(prometheus_config_path + "/rules/alerting_rules.yml").contains(alert_expr)
