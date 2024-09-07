def test_miniflux_is_running(host):
    assert host.service("miniflux").is_running


def test_miniflux_is_enabled(host):
    assert host.service("miniflux").is_enabled


def test_listening_on_port(host):
    assert host.socket("tcp://0.0.0.0:8080").is_listening
