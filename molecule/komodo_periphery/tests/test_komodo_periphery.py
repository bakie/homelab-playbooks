import pytest

KOMODO_GROUP = "komodo"
KOMODO_USER = "komodo"
KOMODO_PERIPHERY_HOME_PATH = "/opt/komodo"
KOMODO_PERIPHERY_INSTALL_PATH = KOMODO_PERIPHERY_HOME_PATH+"/bin"
KOMODO_PERIPHERY_CONFIG_PATH = KOMODO_PERIPHERY_HOME_PATH+"/config"
KOMODO_PERIPHERY_REPO_PATH = KOMODO_PERIPHERY_HOME_PATH+"/repos"
KOMODO_PERIPHERY_STACK_PATH = KOMODO_PERIPHERY_HOME_PATH+"/stacks"
KOMODO_PERIPHERY_BUILD_PATH = KOMODO_PERIPHERY_HOME_PATH+"/builds"


def test_user_is_in_komodo_group(host):
    assert KOMODO_GROUP in host.user(KOMODO_USER).groups


def test_user_is_in_docker_group(host):
    assert "docker" in host.user(KOMODO_USER).groups


def test_komodo_periphery_is_running(host):
    assert host.service("komodo_periphery").is_running


@pytest.mark.parametrize("config", [
    "allowed_ips = \\['127.0.0.1'\\]",
    "passkeys = \\['test_passkey'\\]"
])
def test_komodo_periphery_config(host, config):
    assert host.file(KOMODO_PERIPHERY_CONFIG_PATH+"/config.toml").contains(config)


@pytest.mark.parametrize("path, owner", [
    (KOMODO_PERIPHERY_HOME_PATH, KOMODO_USER),
    (KOMODO_PERIPHERY_INSTALL_PATH, KOMODO_USER),
    (KOMODO_PERIPHERY_CONFIG_PATH, KOMODO_USER),
    (KOMODO_PERIPHERY_REPO_PATH, KOMODO_USER),
    (KOMODO_PERIPHERY_STACK_PATH, KOMODO_USER),
    (KOMODO_PERIPHERY_BUILD_PATH, KOMODO_USER),
])
def test_directory_owner(host, path, owner):
    assert host.file(path).user == owner


@pytest.mark.parametrize("path, group", [
    (KOMODO_PERIPHERY_HOME_PATH, KOMODO_GROUP),
    (KOMODO_PERIPHERY_INSTALL_PATH, KOMODO_GROUP),
    (KOMODO_PERIPHERY_CONFIG_PATH, KOMODO_GROUP),
    (KOMODO_PERIPHERY_REPO_PATH, KOMODO_GROUP),
    (KOMODO_PERIPHERY_STACK_PATH, KOMODO_GROUP),
    (KOMODO_PERIPHERY_BUILD_PATH, KOMODO_GROUP),
])
def test_directory_group(host, path, group):
    assert host.file(path).group == group
