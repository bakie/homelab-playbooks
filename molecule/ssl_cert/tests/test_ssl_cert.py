import pytest

SSL_DIR = "/etc/ssl-dir"


def test_ssl_dir(host):
    assert host.file(SSL_DIR).exists
    assert host.file(SSL_DIR).mode == 0o650


@pytest.mark.parametrize("ssl_file_path, user, group", [
    (SSL_DIR + "/ssl.key", "root", "ssl-cert"),
    (SSL_DIR + "/ssl.crt", "root", "ssl-cert"),
])
def test_ssl_files_user_group(host, ssl_file_path, user, group):
    assert host.file(ssl_file_path).user == user
    assert host.file(ssl_file_path).group == group


@pytest.mark.parametrize("ssl_file_path, mode", [
    (SSL_DIR + "/ssl.key", 0o640),
    (SSL_DIR + "/ssl.crt", 0o640),
])
def test_ssl_files_mode(host, ssl_file_path, mode):
    assert host.file(ssl_file_path).mode == mode


@pytest.mark.parametrize("ssl_file_path, content", [
    (SSL_DIR + "/ssl.key", "content ssl key"),
    (SSL_DIR + "/ssl.crt", "content ssl crt"),
])
def test_ssl_files_content(host, ssl_file_path, content):
    assert host.file(ssl_file_path).contains(content)
