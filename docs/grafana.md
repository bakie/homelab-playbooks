# server.playbooks.grafana
Install and configure agrafana on the remote hosts.

## Requirements
A variable `top_lvl_domain` has to be set for the `grafana_url` default value.

## Role defaults
Available defaults are listed below, along with default value (see [defaults/main.yml](../roles/grafana/defaults/main.yml))
```yaml
grafana_url: "grafana.{{ top_lvl_domain }}"
```
The url used to access Grafana from a web browser.

```yaml
grafana_admin_user: "grafana"
grafana_admin_password: "grafana"
```
The name and password of the default Grafana admin user, who has full permissions. 

```yaml
grafana_group: "grafana"
```
Sets the group for all Grafana files and directories.

```yaml
grafana_version: "10.4.1"
```
Grafana version that should be installed.

```yaml
grafana_plugins:
  - grafana-piechar-panel
```
A list of plugins that should be installed.

```yaml
grafana_listen_port: 3000
```
The port on which Grafana will listen.

```yaml
grafana_config_root_url: "http://{{ grafana_url }}"
```
The full URL used to access Grafana from a web browser.

```yaml
grafana_config_path: "/etc/grafana"
grafana_dashboards_config_path: "{{ grafana_config_path }}/dashboards"
```
Specify the locations for all the directories and files required for Grafana.

```yaml
grafana_datasources:
  - name: Prometheus
    options:
      type: prometheus
      access: proxy
      url: "http://localhost:9090"
```
A list of possible data sources for Grafana.

```yaml
grafana_config_settings:
  - regexp: "^;?admin_user(.*)"
    replace: "admin_user = {{ grafana_admin_user }}"
  - regexp: "^;?admin_password(.*)"
    replace: "admin_password = {{ grafana_admin_password }}"
  - regexp: "^;?root_url(.*)"
    replace: "root_url = {{ grafana_config_root_url }}"
  - regexp: "^;?http_port(.*)"
    replace: "http_port = {{ grafana_listen_port }}"
```
Settings that get configured in the file `{{ grafana_config_path }}/grafana.ini`.

```yaml
grafana_dashboards:
  - src: "dashboards/appliances/openwrt_dashboard.json"
    dest: "{{ grafana_dashboards_config_path }}/appliances"
  - src: "dashboards/application/apps_dashboard.json"
    dest: "{{ grafana_dashboards_config_path }}/application"
  - src: "dashboards/home/utilities_dashboard.json"
    dest: "{{ grafana_dashboards_config_path }}/home"
  - src: "dashboards/server/common_dashboard.json"
    dest: "{{ grafana_dashboards_config_path }}/server"
  - src: "dashboards/server/network_dashboard.json"
    dest: "{{ grafana_dashboards_config_path }}/server"
```
A list of all my Grafana dashboards that need to get copied to the remote host.

## Role variables
Available variables are listed below, along with default value (see [vars/main.yml](../roles/grafana/vars/main.yml))
```yaml
grafana_required_packages: [ "apt-transport-https", "adduser", "libfontconfig", "gnupg2" ]
```
A list of required packages for installing and running Grafana.

```yaml
grafana_apt_key_url: "https://packages.grafana.com/gpg.key"
grafana_apt_repo_url: "deb https://packages.grafana.com/oss/deb stable main"
```
The apt key url and apt repo url from which we will install Grafana.
