import pytest
import yaml


KODI_ADDONS_PATH = "/home/kodi/.kodi/addons"
KODI_ADDONS_SCRIPTS_PATH = "/home/kodi/.kodi/addons_scripts"
KODI_ADDONS_SCRIPTS = [
    "repositories.sh",
    "enable_kodi_addon.sh",
    "get_kodi_addon.sh"
]


@pytest.fixture()
def ansible_defaults():
    with open("roles/kodi/vars/main.yml", 'r') as stream:
        return yaml.full_load(stream)


def test_kodi_group_exists(host):
    assert host.group("kodi").exists


def test_kodi_user_exists(host):
    assert host.user("kodi").exists


def test_kodi_home_dir_exists(host):
    assert host.file("/home/kodi").is_directory


def test_kodi_is_installed(host):
    assert host.package("kodi").is_installed


def test_kodi_version(host, ansible_defaults):
    version = ansible_defaults['kodi_version']
    assert host.package("kodi").version.split("+")[0] == version[:-1]


def test_kodi_is_enabled(host):
    assert host.service("kodi").is_enabled


@pytest.mark.parametrize("config", [
    "allowed_users=anybody",
    "needs_root_rights=yes"
])
def test_x11_wrapper_config(host, config):
    assert host.file("/etc/X11/Xwrapper.config").contains(config)


def test_kodi_pkla_file(host):
    assert host.file("/etc/polkit-1/localauthority/50-local.d/kodi.pkla").exists


@pytest.mark.parametrize("script", KODI_ADDONS_SCRIPTS)
def test_addons_scripts_exist(host, script):
    assert host.file(KODI_ADDONS_SCRIPTS_PATH+"/"+script).exists


@pytest.mark.parametrize("script", KODI_ADDONS_SCRIPTS)
def test_addons_scripts_user(host, script):
    assert host.file(KODI_ADDONS_SCRIPTS_PATH+"/"+script).user == "kodi"


@pytest.mark.parametrize("script", KODI_ADDONS_SCRIPTS)
def test_addons_scripts_group(host, script):
    assert host.file(KODI_ADDONS_SCRIPTS_PATH+"/"+script).group == "kodi"


@pytest.mark.parametrize("addon", [
    "plugin.video.youtube",
    "script.trakt"
])
def test_addon_installed(host, addon):
    assert host.file(KODI_ADDONS_PATH+"/"+addon).is_directory
