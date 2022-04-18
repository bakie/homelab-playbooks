def test_medusa_path_user(host):
    assert host.file("/opt/medusa").user == "medusa"


def test_medusa_path_group(host):
    assert host.file("/opt/medusa").group == "medusa"


def test_medusa_is_running(host):
    assert host.service("medusa").is_running


def test_medusa_is_enabled(host):
    assert host.service("medusa").is_enabled


def test_listening_on_port(host):
    assert host.socket("tcp://0.0.0.0:8081").is_listening
