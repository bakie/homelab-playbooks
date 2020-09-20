import pytest


def test_grafana_is_installed(host):
    assert host.package("grafana").is_installed


def test_grafana_is_running(host):
    assert host.service("grafana-server").is_running


@pytest.mark.parametrize("config", [
    "^admin_user = grafana",
    "^admin_password = grafana",
])
def test_config(host, config):
    assert host.file("/etc/grafana/grafana.ini").contains(config)


def test_config_root_url(host):
    file = host.file("/etc/grafana/grafana.ini")
    assert file.contains("^root_url = http://debian_buster.local",) \
        or file.contains("^root_url = http://ubuntu_focal_fossa.local",)


def test_listening_on_port(host):
    assert host.socket("tcp://0.0.0.0:3000").is_listening


def test_datasources(host):
    assert host.file("/etc/grafana/provisioning/datasources/datasources.yml").exists
