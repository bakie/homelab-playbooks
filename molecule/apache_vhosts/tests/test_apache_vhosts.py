def test_molecule_test_vhost_config_exists(host):
    assert host.file("/etc/apache2/sites-available/molecule_test.conf").exists


def test_molecule_test_vhost_config_symlink(host):
    assert host.file("/etc/apache2/sites-enabled/molecule_test.conf").linked_to == "/etc/apache2/sites-available/molecule_test.conf"
