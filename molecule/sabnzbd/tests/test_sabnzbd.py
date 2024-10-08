import pytest


def test_sabnzbd_group_exists(host):
    assert host.group("sabnzbd").exists


def test_sabnzbd_user_exists(host):
    assert host.user("sabnzbd").exists


@pytest.mark.parametrize("dir", [
    "/opt/sabnzbd",
    "/opt/sabnzbd/.sabnzbd",
    "/opt/sabnzbd/incomplete",
    "/opt/sabnzbd/complete",
    "/opt/sabnzbd/complete/tv",
    "/opt/sabnzbd/complete/movies",
    "/opt/sabnzbd/complete/music",
    "/opt/sabnzbd/nzb"
])
def test_dirs_exists(host, dir):
    assert host.file(dir).is_directory


def test_sabnzbd_runs_as_sabnzbd_user(host):
    file = host.file("/etc/default/sabnzbdplus")
    assert file.contains("USER=sabnzbd")


def test_sabnzbd_is_enabled(host):
    assert host.service("sabnzbdplus").is_enabled


def test_sabnzbd_is_running(host):
    assert host.service("sabnzbdplus").is_running


def test_listening_on_port(host):
    assert host.socket("tcp://0.0.0.0:8080").is_listening


def test_host_whitelist(host):
    if host.system_info.distribution == "debian" and host.system_info.release == "12":
        assert host.file("/opt/sabnzbd/.sabnzbd/sabnzbd.ini").contains("host_whitelist = debian-bookworm-sabnzbd, sabnzbd.local.dev")
    else:
        pytest.fail(f"Unsupported distribution and/or release: {host.system_info.distribution}-{host.system_info.release}")
