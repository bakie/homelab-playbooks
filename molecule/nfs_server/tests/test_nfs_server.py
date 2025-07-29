import pytest


def test_nfs_kernel_server_is_installed(host):
    assert host.package("nfs-kernel-server").is_installed


def test_nfs_kernel_server_is_enabled(host):
    assert host.service("nfs-kernel-server").is_enabled


def test_nfs_kernel_server_is_running(host):
    assert host.service("nfs-kernel-server").is_running


@pytest.mark.parametrize("export", [
    "/home/dir1 host1.local(rw,sync,no_root_squash,no_subtree_check)",
    "/home/dir2/dir host2.local(rw,sync,no_root_squash,no_subtree_check)",
    "/home/dir1/test host3.local(rw,sync,no_root_squash,no_subtree_check)"
])
def test_nfs_server_exports(host, export):
    assert host.file("/etc/exports").contains(export)


@pytest.mark.parametrize("line", [
    "After=network-online.target",
    "Wants=network-online.target"
])
def test_nfs_service_file(host, line):
    assert host.file("/lib/systemd/system/nfs-kernel-server.service").contains(line)
