import pytest
import yaml

PROMETHEUS_NODE_EXPORTER_USER = "prometheus_node_exporter"
PROMETHEUS_NODE_EXPORTER_GROUP = "prometheus_node_exporter"
PROMETHEUS_NODE_EXPORTER_PATH = "/opt/prometheus/node_exporter"
PROMETHEUS_NODE_EXPORTER_BASE_PATH = "/opt/prometheus"
PROMETHEUS_NODE_EXPORTER_CONFIG_PATH = "/etc/prometheus/node_exporter"
PROMETHEUS_NODE_EXPORTER_BASE_CONFIG_PATH = "/etc/prometheus"
PROMETHEUS_NODE_EXPORTER_TEXTFILE_SCRIPTS_PATH = "/etc/prometheus/node_exporter/textfile_scripts"
PROMETHEUS_NODE_EXPORTER_TEXTFILE_SCRIPTS_OUTPUT_PATH = "/etc/prometheus/node_exporter/textfile_scripts_output"


@pytest.fixture()
def ansible_defaults():
    with open("../../roles/prometheus_node_exporter/defaults/main.yml", 'r') as stream:
        return yaml.full_load(stream)


def test_prometheus_node_exporter_group(host):
    assert PROMETHEUS_NODE_EXPORTER_GROUP in host.user(PROMETHEUS_NODE_EXPORTER_USER).groups


@pytest.mark.parametrize("path, owner", [
    (PROMETHEUS_NODE_EXPORTER_PATH, PROMETHEUS_NODE_EXPORTER_USER),
    (PROMETHEUS_NODE_EXPORTER_BASE_PATH, "root"),
    (PROMETHEUS_NODE_EXPORTER_CONFIG_PATH, PROMETHEUS_NODE_EXPORTER_USER),
    (PROMETHEUS_NODE_EXPORTER_BASE_CONFIG_PATH, "root"),
    (PROMETHEUS_NODE_EXPORTER_TEXTFILE_SCRIPTS_PATH, PROMETHEUS_NODE_EXPORTER_USER),
    (PROMETHEUS_NODE_EXPORTER_TEXTFILE_SCRIPTS_OUTPUT_PATH, PROMETHEUS_NODE_EXPORTER_USER)
])
def test_directory_owner(host, path, owner):
    assert host.file(path).user == owner


@pytest.mark.parametrize("path, group", [
    (PROMETHEUS_NODE_EXPORTER_PATH, PROMETHEUS_NODE_EXPORTER_GROUP),
    (PROMETHEUS_NODE_EXPORTER_BASE_PATH, "root"),
    (PROMETHEUS_NODE_EXPORTER_CONFIG_PATH, PROMETHEUS_NODE_EXPORTER_GROUP),
    (PROMETHEUS_NODE_EXPORTER_BASE_CONFIG_PATH, "root"),
    (PROMETHEUS_NODE_EXPORTER_TEXTFILE_SCRIPTS_PATH, PROMETHEUS_NODE_EXPORTER_GROUP),
    (PROMETHEUS_NODE_EXPORTER_TEXTFILE_SCRIPTS_OUTPUT_PATH, PROMETHEUS_NODE_EXPORTER_GROUP)
])
def test_directory_group(host, path, group):
    assert host.file(path).group == group


@pytest.mark.parametrize("path", [
    PROMETHEUS_NODE_EXPORTER_PATH,
    PROMETHEUS_NODE_EXPORTER_BASE_PATH,
    PROMETHEUS_NODE_EXPORTER_CONFIG_PATH,
    PROMETHEUS_NODE_EXPORTER_BASE_CONFIG_PATH,
    PROMETHEUS_NODE_EXPORTER_TEXTFILE_SCRIPTS_PATH,
    PROMETHEUS_NODE_EXPORTER_TEXTFILE_SCRIPTS_OUTPUT_PATH
])
def test_directory_permissions(host, path):
    assert host.file(path).mode == 0o755


def test_prometheus_node_exporter_service_is_running(host):
    assert host.service("prometheus_node_exporter").is_running


def test_prometheus_node_exporter_service_is_enabled(host):
    assert host.service("prometheus_node_exporter").is_enabled


def test_listening_on_port(host):
    assert host.socket("tcp://0.0.0.0:9100").is_listening


@pytest.mark.parametrize("collector", [
    "ntp",
    "systemd",
    "tcpstat",
    "zoneinfo",
    "textfile.directory=/etc/prometheus/node_exporter/textfile"
])
def test_enabled_collectors(host, collector):
    assert host.file("/etc/systemd/system/prometheus_node_exporter.service").contains("--collector." + collector)


@pytest.mark.parametrize("textfile_script", [
    "/apt_check.sh",
    "/fstab_mounts_check.sh"
])
def test_textfile_script(host, textfile_script):
    assert host.file(PROMETHEUS_NODE_EXPORTER_TEXTFILE_SCRIPTS_PATH + textfile_script).exists
    assert host.file(PROMETHEUS_NODE_EXPORTER_TEXTFILE_SCRIPTS_PATH + textfile_script).mode == 0o755


@pytest.mark.parametrize("cron_value", [
    "#Ansible: apt_check",
    "0 \\* \\* \\* \\* /etc/prometheus/node_exporter/textfile_scripts/apt_check.sh /home > /etc/prometheus/node_exporter/textfile_scripts_output/apt_check.prom",
    "#Ansible: fstab_mounts_check",
    "0 \\* \\* \\* \\* /etc/prometheus/node_exporter/textfile_scripts/fstab_mounts_check.sh > /etc/prometheus/node_exporter/textfile_scripts_output/fstab_mounts_check.prom"
])
def test_textfile_cronjob(host, cron_value):
    assert host.file("/var/spool/cron/crontabs/root").contains(cron_value)


def test_version(host, ansible_defaults):
    version = ansible_defaults['prometheus_node_exporter_version']
    assert (host.run(PROMETHEUS_NODE_EXPORTER_PATH+"/node_exporter --version 2>&1 | head -1 | awk '{print $3}' | xargs echo -n").stdout == version)
