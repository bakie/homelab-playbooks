import pytest


def test_openvpn_is_installed(host):
    assert host.package("openvpn").is_installed


def test_default(host):
    assert host.file("/etc/default/openvpn").contains("^AUTOSTART=\"all\"")


def test_openvpn_is_running(host):
    with host.sudo():
        assert host.service("openvpn").is_running


@pytest.mark.parametrize("setting", [
    "remote testRemote 8000",
    "randomCa",
    "randomCert",
    "randomKey",
    "randomTlsAuth"
])
def test_openvpn_client_config(host, setting):
    assert host.file("/etc/openvpn/client.conf").contains(setting)
