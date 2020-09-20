import pytest
import yaml

node_exporter_home = "/opt/node_exporter"
node_exporter_config_path = "/etc/node_exporter/config"


@pytest.fixture()
def AnsibleDefaults():
    with open("../../defaults/main.yml", 'r') as stream:
        return yaml.load(stream)


def test_user(host):
    assert host.group("node_exporter").exists
    assert host.user("node_exporter").exists


@pytest.mark.parametrize("file", [
    node_exporter_home + "/node_exporter",
    node_exporter_config_path + "/config.yml",
    "/lib/systemd/system/node_exporter.service",
])
def test_files(host, file):
    f = host.file(file)
    assert f.exists
    assert f.is_file


@pytest.mark.parametrize("dir", [
    node_exporter_home
])
def test_directories(host, dir):
    d = host.file(dir)
    assert d.is_directory
    assert d.exists


def test_service(host):
    assert host.service("node_exporter").is_running


def test_socket(host):
    s = host.socket("tcp://0.0.0.0:9100")
    assert s.is_listening


def test_version(host, AnsibleDefaults):
    version = AnsibleDefaults['node_exporter_version']
    out = host.run(node_exporter_home + "/node_exporter --version").stderr
    assert "node_exporter, version " + version in out
