# homelab.playbooks.prometheus_blackbox_exporter
Install and configures [blackbox_exporter](https://github.com/prometheus/blackbox_exporter) on the remote hosts.

The blackbox exporter allows blackbox probing of endpoints over HTTP, HTTPS, DNS, TCP and ICMP.

## Requirements
None

## Role defaults
Available defaults are listed below, along with default value (see [defaults/main.yml](../roles/prometheus_blackbox_exporter/defaults/main.yml))
```yaml
prometheus_blackbox_exporter_user: "prometheus_blackbox_exporter"
prometheus_blackbox_exporter_group: "prometheus_blackbox_exporter"
```
Sets the user and group for all prometheus blackbox exporter files and directories. Also sets the user and group that the prometheus_blackbox_exporter process is executed as.

```yaml
prometheus_blackbox_exporter_base_path: "/opt/prometheus"
prometheus_blackbox_exporter_install_path: "{{ prometheus_blackbox_exporter_base_path }}/blackbox_exporter"
prometheus_blackbox_exporter_base_config_path: "/etc/prometheus"
prometheus_blackbox_exporter_config_path: "{{ prometheus_blackbox_exporter_base_config_path }}/blackbox_exporter"
```
The locations for all the directories and files required for prometheus blackbox exporter.

```yaml
prometheus_blackbox_exporter_version: 0.24.0
```
Prometheus blackbox exporter version that should be installed.

```yaml
prometheus_blackbox_exporter_web_listen_address: "0.0.0.0:9103"
```
The address on which prometheus blackbox exporter will listen.

```yaml
prometheus_blackbox_exporter_configuration_modules:
  http_2xx:
    prober: http
    timeout: 5s
    http:
      method: GET
      valid_status_codes: [] # Defaults to 2xx
      preferred_ip_protocol: "ip4"
```
A list of modules that get configured in the file `{{ prometheus_blackbox_exporter_config_path }}/config.yml`. These modules can then be used in the scrape configs (params > module).

## Role variables
Available variables are listed below, along with default value (see [vars/main.yml](../roles/prometheus_blackbox_exporter/vars/main.yml))
```yaml
prometheus_blackbox_exporter_download_url: "https://github.com/prometheus/blackbox_exporter/releases/download/v{{ prometheus_blackbox_exporter_version }}/blackbox_exporter-{{ prometheus_blackbox_exporter_version }}.linux-{{ deb_architecture.stdout }}.tar.gz"
```
The download url for the prometheus blackbox exporter.
