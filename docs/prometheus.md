# Ansible role: prometheus
Install and configure prometheus on the remote hosts.

## Requirements
None.

## Role defaults
Available defaults are listed below, along with default value (see `defaults/main.yml`)

```yaml
prometheus_user: "prometheus"
prometheus_group: "prometheus"
```
Sets the user and group for all prometheus files and directories.

```yaml
prometheus_base_path: "/opt/prometheus"
prometheus_data_path: "{{ prometheus_base_path }}/prometheus_data"
prometheus_base_config_path: "/etc/prometheus"
prometheus_config_path: "{{ prometheus_base_config_path }}/prometheus"
prometheus_alerting_rules_config_path: "{{ prometheus_config_path }}/rules/alerting"
prometheus_recording_rules_config_path: "{{ prometheus_config_path }}/rules/recording"
prometheus_file_sd_config_path: "{{ prometheus_config_path }}/file_sd"
```
Specify the locations for all the directories and files required for prometheus.

```yaml
prometheus_storage_retention: "2y"
```
How long to retain samples in storage.

```yaml
prometheus_version: 2.51.1
```
Prometheus version that should be installed.

```yaml
prometheus_listen_port: 9090
prometheus_listen_address: "0.0.0.0:{{ prometheus_listen_port }}"
```
The port and address on which prometheus will listen.

```yaml
prometheus_alertmanager_address: "127.0.0.1:9093"
```
The address of prometheus alertmanager. Used to configure a static alertmanager instance.

```yaml
prometheus_metrics_job_targets: []
# prometheus_metrics_job_targets:
#   - 10.1.1.1
#   - 10.1.1.50
prometheus_metrics_job_relabel_configs: []
# prometheus_metrics_job_relabel_configs:
#   - source_labels: "[__custom_source_label__]"
#     regex: custom\\.regex\\.test(.*)
#     replacement: custom_replacement
#     target_label: custom_target_label
```
Configuration for the metric job under scrape_configs. This will add targets and relabel_configs.

```yaml
prometheus_blackbox_exporter_address: "127.0.0.1:9103"
```
The address of the blackbox exporter. Used to configure the blackbox exporter under the blackbox job in scrape_configs.

```yaml
prometheus_blackbox_exporter_targets_json_file_sd_path: "{{ prometheus_file_sd_config_path }}/blackbox_exporter_targets.json"
```
The path of the blackbox exporter targets file. Used to configure file_sd_configs under the blackbox job in scrape_configs.

```yaml
prometheus_blackbox_exporter_targets: []
# prometheus_blackbox_exporter_targets:
#   - url: "duckduckgo.com"
#     job: "blackbox"
#   - url: "airvpn.org"
#     job: "blackbox"
```
A list of targets to monitor via the blackbox exporter.
