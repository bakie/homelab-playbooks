import pytest
import yaml

BLACKBOX_EXPORTER_HOME = "/opt/blackbox_exporter"
BLACKBOX_EXPORTER_CONFIG_PATH = "/etc/blackbox_exporter"


@pytest.fixture()
def ansible_defaults():
    with open("roles/blackbox_exporter/defaults/main.yml", 'r') as stream:
        return yaml.full_load(stream)


def test_user(host):
    assert host.group("blackbox_exporter").exists
    assert host.user("blackbox_exporter").exists


@pytest.mark.parametrize("file", [
    BLACKBOX_EXPORTER_HOME + "/blackbox_exporter",
    BLACKBOX_EXPORTER_CONFIG_PATH + "/config.yml",
    "/lib/systemd/system/blackbox_exporter.service",
])
def test_files(host, file):
    f = host.file(file)
    assert f.exists
    assert f.is_file


def test_directories(host):
    d = host.file(BLACKBOX_EXPORTER_HOME)
    assert d.is_directory
    assert d.exists


def test_service(host):
    assert host.service("blackbox_exporter").is_running


def test_socket(host):
    assert host.socket("tcp://0.0.0.0:9101").is_listening


def test_capabilities(host):
    assert "blackbox_exporter = cap_net_raw+ep" in host.run("getcap " + BLACKBOX_EXPORTER_HOME + "/blackbox_exporter").stdout


def test_version(host, ansible_defaults):
    version = ansible_defaults['blackbox_exporter_version']
    out = host.run(BLACKBOX_EXPORTER_HOME + "/blackbox_exporter --version").stderr
    assert "blackbox_exporter, version " + version in out
