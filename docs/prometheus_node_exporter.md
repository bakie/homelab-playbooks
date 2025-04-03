# server.playbooks.prometheus_node_exporter
Install and configure the prometheus node exporter on the remote hosts.

## Requirements
None

## Role defaults
Available defaults are listed below, along with default value (see [defaults/main.yml](../roles/prometheus_node_exporter/defaults/main.yml))
```yaml
prometheus_node_exporter_user: "prometheus_node_exporter"
prometheus_node_exporter_group: "prometheus_node_exporter"
```
Sets the user and group for all prometheus node exporter files and directories. Also sets the user and group that the prometheus_node_exporter process is executed as.

```yaml
prometheus_node_exporter_base_path: "/opt/prometheus"
prometheus_node_exporter_install_path: "{{ prometheus_node_exporter_base_path }}/node_exporter"
prometheus_node_exporter_base_config_path: "/etc/prometheus"
prometheus_node_exporter_config_path: "{{ prometheus_node_exporter_base_config_path }}/node_exporter"
```
The locations for all the directories and files required for prometheus node exporter.

```yaml
prometheus_node_exporter_version: 1.7.0
```
Prometheus node exporter version that should be installed.

```yaml
prometheus_node_exporter_web_listen_address: "0.0.0.0:9100"
```
The address on which prometheus node exporter will listen.

```yaml
prometheus_node_exporter_collectors:
  - systemd
  - tcpstat
  - textfile.directory={{ prometheus_node_exporter_textfile_scripts_output_path }}
```
A List of collectors that get enabled on all remote hosts.

```yaml
prometheus_node_exporter_additional_collectors: []
prometheus_node_exporter_disabled_collectors: []
```
Via these defaults you can add additional collectors or set which collectors need to be disabled per remote hosts.

```yaml
prometheus_node_exporter_textfile_scripts_path: "{{ prometheus_node_exporter_config_path }}/textfile_scripts"
prometheus_node_exporter_textfile_scripts_output_path: "{{ prometheus_node_exporter_config_path }}/textfile_scripts_output"
```
The locations for the scripts files and the output from these scripts. The `prometheus_node_exporter_textfile_scripts_output_path` is used in the textfile collector.

```yaml
prometheus_node_exporter_textfile_scripts:
  - name: apt_check
    script_name: apt_check.sh
    cronjob:
      name: "apt_check"
      minute: "0"
      job: "{{ prometheus_node_exporter_textfile_scripts_path }}/apt_check.sh /home > {{ prometheus_node_exporter_textfile_scripts_output_path }}/apt_check.prom"
    install_on_all_servers: true
  - name: fstab_mounts_check
    script_name: fstab_mounts_check.sh
    cronjob:
      name: "fstab_mounts_check"
      minute: "0"
      job: "{{ prometheus_node_exporter_textfile_scripts_path }}/fstab_mounts_check.sh > {{ prometheus_node_exporter_textfile_scripts_output_path }}/fstab_mounts_check.prom"
    install_on_server_groups: [ "searcher" ]
```
A list of scripts that get added to the remote hosts and have a cronjob configured. The script_name is the name of a script located in the [files/textfile_scripts](../roles/prometheus_node_exporter/files/textfile_scripts) dir. The cronjob gets added to the root user. The `install_on_server_groups` allows to limit on which type of servers the scripts gets installed. The 'install_on_all_servers` option allows to have it installed on all remote hosts.


## Role variables
Available variables are listed below, along with default value (see [vars/main.yml](../roles/prometheus_node_exporter/vars/main.yml))
```yaml
prometheus_node_exporter_download_url: "https://github.com/prometheus/node_exporter/releases/download/v{{ prometheus_node_exporter_version }}/node_exporter-{{ prometheus_node_exporter_version }}.linux-{{ deb_architecture.stdout }}.tar.gz"
```
The download url for the prometheus node exporter.
