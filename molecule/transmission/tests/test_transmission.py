import pytest

TRANSMISSION_INSTALL_PATH = "/opt/transmission"
TRANSMISSION_SETTINGS_PATH = "/opt/transmission/.config/transmission-daemon/settings.json"


def test_default_transmission_group_does_not_exists(host):
    assert not host.group("debian-transmission").exists


def test_default_transmission_user_does_not_exists(host):
    assert not host.user("debian-transmission").exists


def test_default_transmission_dir_does_not_exists(host):
    assert not host.file("/etc/transmission-daemon").exists


def test_transmission_group_exists(host):
    assert host.group("transmission").exists


def test_transmission_user_exists(host):
    assert host.user("transmission").exists


@pytest.mark.parametrize("directory", [
    TRANSMISSION_INSTALL_PATH,
    TRANSMISSION_INSTALL_PATH+"/completed",
    TRANSMISSION_INSTALL_PATH+"/incomplete",
    TRANSMISSION_INSTALL_PATH+"/torrents",
    TRANSMISSION_INSTALL_PATH+"/watchdir"
])
def test_dir_exists(host, directory):
    assert host.file(directory).is_directory


@pytest.mark.parametrize("setting", [
    "\"rpc-username\": \"transmission\"",
    "\"rpc-password\": \"transmission\"",
    "\"alt-speed-down\": 500",
    "\"alt-speed-up\": 1",
    "\"download-dir\": \"/opt/transmission/completed\"",
    "\"encryption\": 2",
    "\"incomplete-dir\": \"/opt/transmission/incomplete\"",
    "\"incomplete-dir-enabled\": true",
    "\"rpc-whitelist-enabled\": false"
])
def test_transmission_settings_file_contains(host, setting):
    assert host.file(TRANSMISSION_SETTINGS_PATH).contains(setting)


def test_transmission_is_running(host):
    assert host.service("transmission-daemon").is_running


def test_transmission_is_enabled(host):
    assert host.service("transmission-daemon").is_enabled


def test_transmission_is_listening(host):
    assert host.socket("tcp://127.0.0.1:9091").is_listening
