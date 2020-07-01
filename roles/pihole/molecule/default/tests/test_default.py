import pytest


def test_pihole_group_exists(host):
    assert host.group("pihole").exists


def test_pihole_user_exists(host):
    assert host.user("pihole").exists


@pytest.mark.parametrize("dir", [
    "/etc/pihole",
    "/opt/pihole"
])
def test_dirs_exists(host, dir):
    assert host.file(dir).is_directory


def test_pihole_is_running(host):
    assert "DNS service is running" in host.run("pihole status").stdout


@pytest.mark.parametrize(("protocol", "port"), [
    ("tcp", "53"),
    ("udp", "53"),
    ("tcp", "80"),
])
def test_listening_on_port(host, protocol, port):
    assert host.socket(protocol + "://0.0.0.0:" + port).is_listening
