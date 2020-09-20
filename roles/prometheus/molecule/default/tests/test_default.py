import pytest
import yaml

prometheus_home = "/opt/prometheus"
prometheus_config_path = "/etc/prometheus"


@pytest.fixture()
def ansible_defaults():
    with open("../../defaults/main.yml", 'r') as stream:
        return yaml.load(stream)


@pytest.mark.parametrize("dir", [
    prometheus_config_path + "/config/rules",
    prometheus_config_path + "/config/file_sd",
    prometheus_config_path + "/config/conf.d"
])
def test_directories(host, dir):
    d = host.file(dir)
    assert d.is_directory
    assert d.exists


@pytest.mark.parametrize("file", [
    prometheus_config_path + "/config/prometheus.yml",
    prometheus_home + "/prometheus",
    prometheus_home + "/promtool",
    prometheus_home + "/tsdb",
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
