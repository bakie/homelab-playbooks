import pytest


@pytest.mark.parametrize("setting", [
    "Unattended-Upgrade::Remove-Unused-Dependencies \"true\";",
    "Unattended-Upgrade::Automatic-Reboot \"true\";",
    "Unattended-Upgrade::Automatic-Reboot-Time \"0[1-3]:[1-5][0-9]\";"
])
def test_50unattended_upgrades_settings(host, setting):
    assert host.file("/etc/apt/apt.conf.d/50unattended-upgrades").contains(setting)


@pytest.mark.parametrize("setting", [
    "APT::Periodic::Update-Package-Lists \"1\";",
    "APT::Periodic::Unattended-Upgrade \"1\";",
    "APT::Periodic::Download-Upgradeable-Packages \"1\";",
    "APT::Periodic::AutocleanInterval \"21\";",
    "APT::Periodic::Verbose \"2\";"
])
def test_20auto_upgrades(host, setting):
    assert host.file("/etc/apt/apt.conf.d/20auto-upgrades").contains(setting)
