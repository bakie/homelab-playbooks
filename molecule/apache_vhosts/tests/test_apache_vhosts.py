import pytest


@pytest.mark.parametrize("vhost", [
    "molecule_proxy_pass_http.conf",
    "molecule_proxy_pass_https.conf",
    "molecule_document_root_http.conf",
    "molecule_document_root_https.conf"
])
def test_molecule_vhost_config_exists(host, vhost):
    assert host.file("/etc/apache2/sites-available/" + vhost).exists


@pytest.mark.parametrize("vhost", [
    "molecule_proxy_pass_http.conf",
    "molecule_proxy_pass_https.conf",
    "molecule_document_root_http.conf",
    "molecule_document_root_https.conf"
])
def test_molecule_vhost_config_symlink(host, vhost):
    assert host.file("/etc/apache2/sites-enabled/" + vhost).linked_to == "/etc/apache2/sites-available/" + vhost


@pytest.mark.parametrize("config", [
    "ServerName molecule_proxy_pass_http.random.url",
    "ProxyPass / http://0.0.0.0:9003",
    "ProxyPassReverse / http://0.0.0.0:9003",
    "CustomLog ${APACHE_LOG_DIR}/molecule_proxy_pass_http.access.log log"
])
def test_molecule_proxy_pass_http_vhost(host, config):
    assert host.file("/etc/apache2/sites-available/molecule_proxy_pass_http.conf").contains(config)


@pytest.mark.parametrize("config", [
    "<VirtualHost \\*:443>",
    "SSLCertificateFile",
    "SSLCertificateKeyFile"
])
def test_molecule_proxy_pass_http_does_not_contain_https_config(host, config):
    assert not host.file("/etc/apache2/sites-available/molecule_proxy_pass_http.conf").contains(config)


@pytest.mark.parametrize("config", [
    "<VirtualHost \\*:443>",
    "SSLCertificateFile",
    "SSLCertificateKeyFile"
])
def test_molecule_proxy_pass_https_contains_https_config(host, config):
    assert host.file("/etc/apache2/sites-available/molecule_proxy_pass_https.conf").contains(config)


@pytest.mark.parametrize("config", [
    "ServerName molecule_document_root_http.random.url",
    "DocumentRoot /var/www/html/",
    "Directory /var/www/html/",
    "CustomLog ${APACHE_LOG_DIR}/molecule_document_root_http.access.log log"
])
def test_molecule_document_root_http_vhost(host, config):
    assert host.file("/etc/apache2/sites-available/molecule_document_root_http.conf").contains(config)


@pytest.mark.parametrize("config", [
    "<VirtualHost \\*:443>",
    "SSLCertificateFile",
    "SSLCertificateKeyFile"
])
def test_molecule_document_root_http_does_not_contain_https_config(host, config):
    assert not host.file("/etc/apache2/sites-available/molecule_document_root_http.conf").contains(config)


@pytest.mark.parametrize("config", [
    "<VirtualHost \\*:443>",
    "SSLCertificateFile",
    "SSLCertificateKeyFile"
])
def test_molecule_document_root_https_contains_https_config(host, config):
    assert host.file("/etc/apache2/sites-available/molecule_document_root_https.conf").contains(config)
