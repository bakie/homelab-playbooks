import pytest


def test_openvpn_is_running(host):
    assert host.service("openvpn").is_running


def test_openvpn_is_enabled(host):
    assert host.service("openvpn").is_enabled


def test_default(host):
    assert host.file("/etc/default/openvpn").contains("^AUTOSTART=\"all\"")


def test_openvpn_testName_is_enabled(host):
    assert host.service("openvpn@testName.service").is_enabled


@pytest.mark.parametrize("setting", [
    "remote testRemote 8000",
    "randomCa",
    "randomCert",
    "randomKey",
    "randomTlsAuth"
])
def test_openvpn_client_config(host, setting):
    assert host.file("/etc/openvpn/testName.conf").contains(setting)
