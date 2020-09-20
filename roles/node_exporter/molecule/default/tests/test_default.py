import pytest
import yaml

prometheus_node_exporter_home = "/opt/prometheus_node_exporter"
prometheus_node_exporter_config_path = "/etc/prometheus_node_exporter/config"


@pytest.fixture()
def AnsibleDefaults():
    with open("../../defaults/main.yml", 'r') as stream:
        return yaml.load(stream)


def test_user(host):
    assert host.group("prometheus_node_exporter").exists
    assert host.user("prometheus_node_exporter").exists


@pytest.mark.parametrize("file", [
    prometheus_node_exporter_home + "/node_exporter",
    prometheus_node_exporter_config_path + "/config.yml",
    "/lib/systemd/system/prometheus_node_exporter.service",
])
def test_files(host, file):
    f = host.file(file)
    assert f.exists
    assert f.is_file


@pytest.mark.parametrize("dir", [
    prometheus_node_exporter_home
])
def test_directories(host, dir):
    d = host.file(dir)
    assert d.is_directory
    assert d.exists


def test_service(host):
    assert host.service("prometheus_node_exporter").is_running


def test_socket(host):
    s = host.socket("tcp://0.0.0.0:9100")
    assert s.is_listening


def test_version(host, AnsibleDefaults):
    version = AnsibleDefaults['prometheus_node_exporter_version']
    out = host.run(prometheus_node_exporter_home + "/node_exporter --version").stderr
    assert "node_exporter, version " + version in out
