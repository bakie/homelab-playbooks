import pytest
import yaml

prometheus_home = "/opt/prometheus"


@pytest.fixture()
def AnsibleDefaults():
    with open("../../defaults/main.yml", 'r') as stream:
        return yaml.load(stream)


@pytest.mark.parametrize("dir", [
    prometheus_home + "/config/rules",
    prometheus_home + "/config/file_sd",
    prometheus_home + "/config/conf.d"
])
def test_directories(host, dir):
    d = host.file(dir)
    assert d.is_directory
    assert d.exists


@pytest.mark.parametrize("file", [
    prometheus_home + "/config/prometheus.yml",
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


def test_version(host, AnsibleDefaults):
    version = AnsibleDefaults['prometheus_version']
    out = host.run(prometheus_home + "/prometheus --version").stderr
    assert "prometheus, version " + version in out
