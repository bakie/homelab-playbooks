def test_resolvconf_is_installed(host):
    assert host.package("resolvconf").is_installed


def test_dns_resolver_ip_in_settings(host):
    assert host.file("/etc/resolvconf/resolv.conf.d/tail").contains("nameserver 10.1.1.25")
