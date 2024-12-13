import pytest


def test_openvpn_is_running(host):
    assert host.service("openvpn").is_running


def test_openvpn_is_enabled(host):
    assert host.service("openvpn").is_enabled


def test_default(host):
    assert host.file("/etc/default/openvpn").contains("^AUTOSTART=\"all\"")


def test_openvpn_testName_is_enabled(host):
    assert host.service("openvpn@dummy.service").is_enabled


def test_openvpn_auth_user_pass_file_path(host):
    assert host.file("/etc/openvpn/auth_user_pass").mode == 0o600


@pytest.mark.parametrize("setting", [
    "molecule_username",
    "molecule_password"
])
def test_openvpn_auth_user_pass(host, setting):
    assert host.file("/etc/openvpn/auth_user_pass").contains(setting)


def test_openvpn_client_config(host):
    assert host.file("/etc/openvpn/dummy.conf").contains("auth-user-pass /etc/openvpn/auth_user_pass")
