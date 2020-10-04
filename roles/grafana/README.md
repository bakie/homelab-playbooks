## Role Variables

### grafana_group
The group for the grafana user

Default value is "grafana"

### grafana_url
The url for grafana which is used in the apache vhost

Default value is "grafana.{{ top_lvl_domain }}"

### grafana_admin_user
The username for the grafana login

Default value is "grafana"

###grafana_admin_password
The password for the grafana login

Default value is "grafana"

### grafana_config_root_url
The url for grafana which is used in the grafana config file

Default value is "http://{{ grafana_url }}"

### grafana_config_path
The path of the configuration files

Default value is "/etc/grafana"

### grafana_listen_port
The port on which grafana should listen

Default value is 3000

### grafana_datasources
A list of datasources that will be added to the provisioning dir of grafana

Default value is
```
grafana_datasources:
  - name: Prometheus
    options:
      type: prometheus
      access: proxy
      url: "http://prometheus.local:9090"
```

### grafana_config_settings
A list of config settings

Default value is
```
grafana_config_settings:
  - regexp: "^;?admin_user(.*)"
    replace: "admin_user = {{ grafana_admin_user }}"
  - regexp: "^;?admin_password(.*)"
    replace: "admin_password = {{ grafana_admin_password }}"
  - regexp: "^;?root_url(.*)"
    replace: "root_url = {{ grafana_config_root_url }}"
  - regexp: "^;?http_port(.*)"
    replace: "http_port = {{ grafana_http_port }}"
```

### grafana_dashboards_config_path
The path to the location of the dashboards json configs

Default value is "/etc/grafana/dashboards"

### grafana_dashboards
A list of src and dest of grafana dashboard in json format.
The src will be searched in the files directory of the role.

Default value is
```
  - src: "application/apps_dashboard.json"
    dest: "{{ grafan_dashboards_config_path }}/application"
  - src: "server/common_dashboard.json"
    dest: "{{ grafan_dashboards_config_path }}/server"
  - src: "server/network_dashboard.json"
    dest: "{{ grafan_dashboards_config_path }}/server"
```
