import pytest


def test_vikunja_path_user(host):
    assert host.file("/opt/vikunja").user == "vikunja"


def test_vikunja_path_group(host):
    assert host.file("/opt/vikunja").group == "vikunja"


def test_vikunja_is_running(host):
    assert host.service("vikunja").is_running


def test_vikunja_is_enabled(host):
    assert host.service("vikunja").is_enabled


def test_listening_on_port(host):
    assert host.socket("tcp://127.0.0.1:8080").is_listening


@pytest.mark.parametrize("setting", [
    "interface: \"127.0.0.1:8080\"",
    "timezone: GMT"
])
def test_config_settings(host, setting):
    assert host.file("/etc/vikunja/config.yml").contains(setting)
