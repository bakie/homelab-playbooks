import pytest
import yaml

NODE_EXPORTER_HOME = "/opt/node_exporter"
NODE_EXPORTER_CONFIG_PATH = "/etc/node_exporter"


@pytest.fixture()
def ansible_defaults():
    with open("roles/node_exporter/vars/main.yml", 'r') as stream:
        return yaml.full_load(stream)


def test_user(host):
    assert host.group("node_exporter").exists
    assert host.user("node_exporter").exists


@pytest.mark.parametrize("file", [
    NODE_EXPORTER_HOME + "/node_exporter",
    NODE_EXPORTER_CONFIG_PATH + "/config.yml",
    "/lib/systemd/system/node_exporter.service",
])
def test_files(host, file):
    f = host.file(file)
    assert f.exists
    assert f.is_file


def test_directories(host):
    d = host.file(NODE_EXPORTER_HOME)
    assert d.is_directory
    assert d.exists


def test_service(host):
    assert host.service("node_exporter").is_running


def test_socket(host):
    s = host.socket("tcp://0.0.0.0:9100")
    assert s.is_listening


def test_version(host, ansible_defaults):
    version = ansible_defaults['node_exporter_version']
    out = host.run(NODE_EXPORTER_HOME + "/node_exporter --version").stderr
    assert "node_exporter, version " + version in out
