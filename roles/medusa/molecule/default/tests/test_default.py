def test_medusa_dir_exists(host):
    assert host.file("/opt/medusa").exists


def test_medusa_permissions(host):
    assert host.file("/opt/medusa/start.py").user == "medusa"
    assert host.file("/opt/medusa/start.py").group == "medusa"


def test_service_file_exists(host):
    assert host.file("/etc/systemd/system/medusa.service").exists


def test_medusa_is_enabled(host):
    assert host.service("medusa").is_enabled


def test_medusa_is_running(host):
    with host.sudo():
        assert host.service("medusa").is_running


def test_listening_on_port(host):
    assert host.socket("tcp://0.0.0.0:8081").is_listening
