import pytest


@pytest.mark.parametrize("vhost", [
    "molecule_http.conf",
    "molecule_https.conf"
])
def test_molecule_vhost_config_exists(host, vhost):
    assert host.file("/etc/apache2/sites-available/" + vhost).exists


@pytest.mark.parametrize("vhost", [
    "molecule_http.conf",
    "molecule_https.conf"
])
def test_molecule_vhost_config_symlink(host, vhost):
    assert host.file("/etc/apache2/sites-enabled/" + vhost).linked_to == "/etc/apache2/sites-available/" + vhost


@pytest.mark.parametrize("config", [
    "ServerName molecule_http.random.url",
    "ProxyPass / http://0.0.0.0:9003",
    "ProxyPassReverse / http://0.0.0.0:9003",
    "CustomLog ${APACHE_LOG_DIR}/molecule_http.access.log log"
])
def test_molecule_http_vhost(host, config):
    assert host.file("/etc/apache2/sites-available/molecule_http.conf").contains(config)


@pytest.mark.parametrize("config", [
    "<VirtualHost \\*:443>",
    "SSLCertificateFile",
    "SSLCertificateKeyFile"
])
def test_molecule_http_does_not_contain_https_config(host, config):
    assert not host.file("/etc/apache2/sites-available/molecule_http.conf").contains(config)


@pytest.mark.parametrize("config", [
    "<VirtualHost \\*:443>",
    "SSLCertificateFile",
    "SSLCertificateKeyFile"
])
def test_molecule_https_contains_https_config(host, config):
    assert host.file("/etc/apache2/sites-available/molecule_https.conf").contains(config)
