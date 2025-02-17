import pytest

GOTIFY_GROUP = "gotify"
GOTIFY_USER = "gotify"
GOTIFY_INSTALL_PATH = "/opt/gotify"
GOTIFY_CONFIG_PATH = "/etc/gotify"
GOTIFY_CONFIG_FILE_PATH = "/etc/gotify/config.yml"


def test_user_is_in_gotify_group(host):
    assert GOTIFY_GROUP in host.user(GOTIFY_USER).groups


def test_directory_owner(host):
    assert host.file(GOTIFY_CONFIG_PATH).user == GOTIFY_USER


def test_directory_group(host):
    assert host.file(GOTIFY_CONFIG_PATH).group == GOTIFY_GROUP


def test_directory_permissions(host):
    assert host.file(GOTIFY_CONFIG_PATH).mode == 0o755


@pytest.mark.parametrize("config_setting", [
    "listenaddr: \"127.0.0.1\"",
    "port: 9090",
    "name: admin",
    "pass: admin"
])
def test_config(host, config_setting):
    assert host.file(GOTIFY_CONFIG_FILE_PATH).contains(config_setting)
