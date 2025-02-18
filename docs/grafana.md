# server.playbooks.grafana
Install and configure agrafana on the remote hosts.

## Requirements
None

## Role variables
| Variable               | Default                        | Comments |
|------------------------|--------------------------------|----------|
| grafana_url            | "grafana.{{ top_lvl_domain }}" |          |
| grafana_admin_user     | "grafana"                      |          |
| grafana_admin_password | "grafana"                      |          |
| grafana_group          | "grafana"                      |          |
| grafana_required_packages | [ "apt-transport-https", "adduser", "libfontconfig", "gnupg2" ] | Array of required packages to run grafana |
| grafana_apt_key_url    | "https://packages.grafana.com/gpg.key" |  |
| grafana_apt_repo_url   | "deb https://packages.grafana.com/oss/deb stable main" |  |
| grafana_version        | "10.4.1"                       |          |
| grafana_plugins        | <pre>- grafana-piechar-panel</pre>       | List of plugins to install |
| grafana_config_root_url | "http://{{ grafana_url }}"    | full URL used to access Grafana from a web browser |
| grafana_config_path    | "/etc/grafana"                 |          |
| grafana_listen_port    | 3000                           |          |
| grafana_datasources    | <pre>- name: Prometheus<br>  options:<br>    type: prometheus<br>    access: proxy<br>    url: "http://localhost:9090</pre> |  |
| grafana_config_settings | <pre>- regexp: "^;?admin_user(.\*)"<br>  replace: "admin_user = {{ grafana_admin_user }}"<br>- regexp: "^;?admin_password(.\*)"<br>  replace: "admin_password = {{ grafana_admin_password }}"<br>- regexp: "^;?root_url(.\*)"<br>  replace: "root_url = {{ grafana_config_root_url }}"<br>- regexp: "^;?http_port(.\*)"<br>  replace: "http_port = {{ grafana_listen_port }}"<br></pre> | |
| grafana_dashboards_config_path | "{{ grafana_config_path }}/dashboards" | |
| grafana_dashboard | <pre>- src: "dashboards/appliances/openwrt_dashboard.json"<br>  dest: "{{ grafana_dashboards_config_path }}/appliances"<br>- src: "dashboards/application/apps_dashboard.json"<br>  dest: "{{ grafana_dashboards_config_path }}/application"<br>- src: "dashboards/home/utilities_dashboard.json"<br>  dest: "{{ grafana_dashboards_config_path }}/home"<br>- src: "dashboards/server/common_dashboard.json"<br>  dest: "{{ grafana_dashboards_config_path }}/server"<br>- src: "dashboards/server/network_dashboard.json"<br>  dest: "{{ grafana_dashboards_config_path }}/server"</pre> | |
