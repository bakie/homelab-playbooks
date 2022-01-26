import pytest


PIHOLE_CONFIG_PATH = "/etc/pihole"


def test_pihole_group_exists(host):
    assert host.group("pihole").exists


def test_pihole_user_exists(host):
    assert host.user("pihole").exists


@pytest.mark.parametrize("dir", [
    PIHOLE_CONFIG_PATH,
    "/opt/pihole"
])
def test_dirs_exists(host, dir):
    assert host.file(dir).is_directory


def test_pihole_is_running(host):
    assert "FTL is listening" in host.run("pihole status").stdout


@pytest.mark.parametrize(("protocol", "port"), [
    ("tcp", "53"),
    ("udp", "53"),
    ("tcp", "80"),
])
def test_listening_on_port(host, protocol, port):
    assert host.socket(protocol + "://0.0.0.0:" + port).is_listening


@pytest.mark.parametrize("dns_entry", [
    "10.1.1.100 pihole.custom.dns",
    "10.1.1.83 pihole_test.custom.dns"
])
def test_custom_dns_entries(host, dns_entry):
    assert host.file(PIHOLE_CONFIG_PATH + "/custom.list").contains(dns_entry)


def test_firebog_lists(host):
    assert host.file(PIHOLE_CONFIG_PATH + "/list.1.raw.githubusercontent.com.domains").exists


def test_adlist_count(host):
    assert int(host.run("sqlite3 " + PIHOLE_CONFIG_PATH + "/gravity.db 'select count(*) from adlist;'").stdout) > 10


def test_cronjob(host):
    assert host.file("/var/spool/cron/crontabs/pihole").contains(
        "wget -qO - https://v.firebog.net/hosts/lists.php?type=nocross | "
        "xargs -I {} sqlite3 /etc/pihole/gravity.db 'INSERT OR IGNORE INTO adlist (Address) VALUES ('{}');' "
        "&& sudo pihole -g")


def test_sudoers(host):
    assert host.file("/etc/sudoers.d/pihole").contains("pihole ALL=(ALL) NOPASSWD:/usr/local/bin/pihole")
