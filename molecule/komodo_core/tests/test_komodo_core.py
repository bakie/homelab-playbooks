import pytest

KOMODO_GROUP = "komodo"
KOMODO_USER = "komodo"
KOMODO_INSTALL_PATH = "/opt/komodo"


def test_user_is_in_komodo_group(host):
    assert KOMODO_GROUP in host.user(KOMODO_USER).groups


def test_user_is_in_docker_group(host):
    assert "docker" in host.user(KOMODO_USER).groups


def test_komodo_core_is_running(host):
    assert host.socket("tcp://0.0.0.0:9120").is_listening


@pytest.mark.parametrize("container_name", [
    "komodo-core-1",
    "komodo-ferretdb-1",
    "komodo-postgres-1"
])
def test_komodo_containers_are_running(host, container_name):
    assert container_name in host.run("docker ps --format \"{{.Names}}\" | xargs echo -n").stdout.split(' ')
