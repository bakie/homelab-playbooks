import pytest
import yaml

PROMETHEUS_ALERTMANAGER_HOME = "/opt/prometheus_alertmanager"


@pytest.fixture()
def ansible_defaults():
    with open("roles/prometheus_alertmanager/vars/main.yml", 'r') as stream:
        return yaml.full_load(stream)


@pytest.mark.parametrize("file", [
    "/etc/alertmanager/alertmanager.yml",
    "/etc/amtool/config.yml",
    PROMETHEUS_ALERTMANAGER_HOME + "/alertmanager",
    PROMETHEUS_ALERTMANAGER_HOME + "/amtool",
    "/lib/systemd/system/alertmanager.service",
])
def test_files(host, file):
    f = host.file(file)
    assert f.exists
    assert f.is_file


def test_user(host):
    assert host.group("alertmanager").exists
    assert host.user("alertmanager").exists


def test_service_is_running(host):
    assert host.service("alertmanager").is_running


def test_service_is_enabled(host):
    assert host.service("alertmanager").is_enabled


def test_socket(host):
    assert host.socket("tcp://127.0.0.1:9093").is_listening


def test_version(host, ansible_defaults):
    version = ansible_defaults['prometheus_alertmanager_version']
    out = host.run(PROMETHEUS_ALERTMANAGER_HOME + "/alertmanager --version").stdout
    assert "alertmanager, version " + version in out
