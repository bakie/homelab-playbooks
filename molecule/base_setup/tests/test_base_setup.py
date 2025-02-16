import pytest


@pytest.mark.parametrize("package", [
    "python3-apt",
    "aptitude",
    "curl",
    "htop",
    "rsync",
    "sudo",
    "vim",
    "build-essential",
    "acl"
])
def test_package_installed(host, package):
    assert host.package(package).is_installed


def test_keep_home_sudoers(host):
    assert host.file("/etc/sudoers.d/keep-home").contains("Defaults    env_keep += \"HOME\"")
