import pytest


@pytest.mark.parametrize("package", [
    "python3-apt",
    "aptitude",
    "curl",
    "htop",
    "rsync",
    "sudo",
    "vim",
    "build-essential"
])
def test_package_installed(host, package):
    assert host.package(package).is_installed
