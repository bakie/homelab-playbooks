import pytest


GRAFANA_CONFIG_PATH = "/etc/grafana"


def test_grafana_is_installed(host):
    assert host.package("grafana").is_installed


def test_grafana_is_running(host):
    assert host.service("grafana-server").is_running


@pytest.mark.parametrize("config", [
    "^admin_user = grafana",
    "^admin_password = grafana",
])
def test_config(host, config):
    assert host.file(GRAFANA_CONFIG_PATH + "/grafana.ini").contains(config)


def test_config_root_url(host):
    file = host.file(GRAFANA_CONFIG_PATH + "/grafana.ini")
    assert file.contains("^root_url = http://grafana.homelab.net",)


def test_listening_on_port(host):
    assert host.socket("tcp://0.0.0.0:3000").is_listening


def test_datasources_provisioning(host):
    assert host.file(GRAFANA_CONFIG_PATH + "/provisioning/datasources/datasources.yaml").exists


def test_dashboards_provisioning(host):
    assert host.file(GRAFANA_CONFIG_PATH + "/provisioning/dashboards/dashboards.yaml").exists


@pytest.mark.parametrize("dashboard", [
    "server/common_dashboard.json",
    "server/network_dashboard.json",
    "application/apps_dashboard.json",
    "appliances/openwrt_dashboard.json"
])
def test_dashboards(host, dashboard):
    assert host.file("/etc/grafana/dashboards/" + dashboard).exists
