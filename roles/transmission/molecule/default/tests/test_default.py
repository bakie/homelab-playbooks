import pytest


TRANSMISSION_SETTINGS_PATH = "/opt/transmission/.config/transmission-daemon/settings.json"


def test_transmission_group_exists(host):
    assert host.group("debian-transmission").exists


def test_transmission_user_exists(host):
    assert host.user("debian-transmission").exists


@pytest.mark.parametrize("directory", [
    "/opt/transmission",
    "/opt/transmission/completed",
    "/opt/transmission/incomplete",
    "/opt/transmission/torrents",
    "/opt/transmission/watchdir"
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


def test_apache_vhost_sites_available(host):
    assert host.file("/etc/apache2/sites-available/transmission.conf").exists


def test_apache_vhost_sites_enabled(host):
    assert host.file("/etc/apache2/sites-enabled/transmission.conf").is_symlink
