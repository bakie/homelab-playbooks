import pytest
import yaml

blackbox_exporter_home = "/opt/blackbox_exporter"
blackbox_exporter_config_path = "/etc/blackbox_exporter"


@pytest.fixture()
def AnsibleDefaults():
    with open("../../defaults/main.yml", 'r') as stream:
        return yaml.load(stream)


def test_user(host):
    assert host.group("blackbox_exporter").exists
    assert host.user("blackbox_exporter").exists


@pytest.mark.parametrize("file", [
    blackbox_exporter_home + "/blackbox_exporter",
    blackbox_exporter_config_path + "/config.yml",
    "/lib/systemd/system/blackbox_exporter.service",
])
def test_files(host, file):
    f = host.file(file)
    assert f.exists
    assert f.is_file


@pytest.mark.parametrize("dir", [
    blackbox_exporter_home
])
def test_directories(host, dir):
    d = host.file(dir)
    assert d.is_directory
    assert d.exists


def test_service(host):
    assert host.service("blackbox_exporter").is_running


def test_socket(host):
    s = host.socket("tcp://0.0.0.0:9101")
    assert s.is_listening


def test_capabilities(host):
    assert "blackbox_exporter = cap_net_raw+ep" in host.run("getcap " + blackbox_exporter_home + "/blackbox_exporter").stdout


def test_version(host, AnsibleDefaults):
    version = AnsibleDefaults['blackbox_exporter_version']
    out = host.run(blackbox_exporter_home + "/blackbox_exporter --version").stderr
    assert "blackbox_exporter, version " + version in out
