# server.playbooks.prometheus_alertmanager
Install and configure prometheus alertmanager on the remote hosts.

## Requirements
The [Gotify](gotify.md) service is required for using this role. We use the gotify bridge to send notifictions to Gotify.

## Role defaults
Available defaults are listed below, along with default value (see [defaults/main.yml](../roles/prometheus_alertmanager/defaults/main.yml))
```yaml
prometheus_alertmanager_user: "prometheus_alertmanager"
prometheus_alertmanager_group: "prometheus_alertmanager"
```
Sets the user and group for all prometheus alertmanager files and directories. Also sets the user and group that the prometheus_alertmanager process is executed as.

```yaml
prometheus_alertmanager_base_path: "/opt/prometheus"
prometheus_alertmanager_install_path: "{{ prometheus_alertmanager_base_path }}/alertmanager"
prometheus_alertmanager_data_path: "{{ prometheus_alertmanager_base_path }}/alertmanager_data"
prometheus_alertmanager_base_config_path: "/etc/prometheus"
prometheus_alertmanager_config_path: "{{ prometheus_alertmanager_base_config_path }}/alertmanager"
prometheus_alertmanager_amtool_config_path: "/etc/amtool"
prometheus_alertmanager_amtool_config_file_path: "{{ prometheus_alertmanager_amtool_config_path }}/config.yml"
```
The locations for all the directories and files required for prometheus alertmanager. The `prometheus_alertmanager_amtool_config_path` needs to be either `/etc/amtool` or `$HOME/.config/amtool/config.yml`.

```yaml
prometheus_alertmanager_version: 0.27.0
```
Prometheus alertmanager version that should be installed.

```yaml
prometheus_alertmanager_web_listen_address: "0.0.0.0:{{ prometheus_alertmanager_listen_port }}"
prometheus_alertmanager_listen_port: 9093
```
The port and address on which prometheus alertmanager will listen.

```yaml
prometheus_alertmanager_amtool_url: "http://127.0.0.1:{{ prometheus_alertmanager_listen_port }}"
```
The url for amtool which is configured in the config file `prometheus_alertmanager_amtool_config_file_path`.

```yaml
prometheus_alertmanager_webhook_url: "http://{{ prometheus_alertmanager_gotify_bridge_bind_address }}:{{ prometheus_alertmanager_gotify_bridge_port }}{{ prometheus_alertmanager_gotify_bridge_webhook_path }}"
```
The endpoint to send HTTP POST requests to from prometheus alertmanager. This should be the gotify bridge component url.

```yaml
prometheus_alertmanager_gotify_bridge_path: "{{ prometheus_alertmanager_base_path }}/alertmanager_gotify_bridge"
prometheus_alertmanager_gotify_bridge_install_path: "{{ prometheus_alertmanager_gotify_bridge_path }}"
```
The locations for the gotify bridge component.

```yaml
prometheus_alertmanager_gotify_bridge_version: "v2.3.0"
```
Gotify bridge version that should be installed.

```yaml
prometheus_alertmanager_gotify_bridge_bind_address: 127.0.0.1
prometheus_alertmanager_gotify_bridge_port: 8080
```
The port and address on which the gotify service is listening.

```yaml
prometheus_alertmanager_gotify_bridge_webhook_path: "/gotify_webhook"
```
The webhook path on which the gotify bridge will handle requests on.

```yaml
prometheus_alertmanager_gotify_endpoint: "http://localhost/message"
```
Full path to the Gotify service message endpoint.

```yaml
prometheus_alertmanager_gotify_token: "dummyToken"
```
The token generated in Gotify which gets configured in 

## Role variables
Available variables are listed below, along with default value (see [vars/main.yml](../roles/blackbox_exporter/vars/main.yml))
```yaml
prometheus_alertmanager_download_url: "https://github.com/prometheus/alertmanager/releases/download/v{{ prometheus_alertmanager_version }}/alertmanager-{{ prometheus_alertmanager_version }}.linux-{{ deb_architecture.stdout }}.tar.gz"
prometheus_alertmanager_gotify_bridge_download_url: "https://github.com/DRuggeri/alertmanager_gotify_bridge/releases/download/{{ prometheus_alertmanager_gotify_bridge_version }}/alertmanager_gotify_bridge-{{ prometheus_alertmanager_gotify_bridge_version }}-linux-{{ deb_architecture.stdout }}"
```
The download urls for the alertmanager and the gotify bridge component.
