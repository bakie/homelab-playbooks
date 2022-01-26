def test_nfs_common_is_installed(host):
    assert host.package("nfs-common").is_installed


def test_local_dir_exists(host):
    assert host.file("/media/dir").is_directory


def test_nfs_exports(host):
    assert host.file("/etc/fstab").contains("10.1.1.1:/home/user/dir")
