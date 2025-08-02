def test_docker_ce_is_installed(host):
    assert host.package("docker-ce").is_installed


def test_docker_cli_is_installed(host):
    assert host.package("docker-ce-cli").is_installed


def test_docker_is_running(host):
    assert host.service("docker").is_running
