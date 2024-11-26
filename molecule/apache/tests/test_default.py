import pytest


def test_apache_is_installed(host):
    assert host.package("apache2").is_installed


def test_apache_is_running(host):
    assert host.service("apache2").is_running


@pytest.mark.parametrize("name", [
    "autoindex",
    "deflate",
    "expires",
    "filter",
    "headers",
    "http2",
    "include",
    "mime",
    "rewrite",
    "setenvif",
    "ssl",
    "proxy_html",
    "proxy_http",
    "proxy_wstunnel",
    "xml2enc"
])
def test_modules_are_enabled(host, name):
    assert host.file("/etc/apache2/mods-enabled/" + name + ".load").exists


@pytest.mark.parametrize("name", [
    "hostname",
    "security"
])
def test_configs_are_enabled(host, name):
    assert host.file("/etc/apache2/conf-enabled/" + name + ".conf").exists


@pytest.mark.parametrize("value", [
    "ServerTokens Prod",
    "ServerSignature Off"
])
def test_security_conf_settings(host, value):
    assert host.file("/etc/apache2/conf-available/security.conf").contains(value)


def test_ssl_settings(host):
    assert host.file("/etc/apache2/mods-available/ssl.conf").contains("SSLCipherSuite HIGH:!aNULL:!SHA1")


@pytest.mark.parametrize("listen", [
    "Listen 0.0.0.0:80",
    "Listen 0.0.0.0:443"
])
def test_apache_listen_ports(host, listen):
    assert host.file("/etc/apache2/ports.conf").contains(listen)


@pytest.mark.parametrize("port", [
    "80",
    "443"
])
def test_listening_on_port(host, port):
    assert host.socket("tcp://0.0.0.0:"+port).is_listening
