import pytest


def test_nfs_common_is_installed(host):
    assert host.package("nfs-common").is_installed


@pytest.mark.parametrize("dir", [
    "/media/dir",
    "/media/dir2"
])
def test_local_dir_exists(host, dir):
    assert host.file(dir).is_directory


@pytest.mark.parametrize(("dir", "mode"), [
    ("/media/dir", 0o755),
    ("/media/dir2", 0o640)
])
def test_local_dir_mode(host, dir, mode):
    assert host.file(dir).mode == mode


def test_nfs_server_exports(host):
    assert host.file("/etc/fstab").contains("10.1.1.1:/home/user/dir")
