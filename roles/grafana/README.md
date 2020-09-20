## Role Variables

### grafana_url
The url for grafana which is used in the apache vhost

Default value is "{{ inventory_hostname }}.local"

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

### grafana_http_port
The port on which grafana should listen

Default value is 3000


### grafana_datasources
A lists of datasources that will be added to the provisioning dir of grafana

Default value is
```
grafana_datasources:
  - name: Prometheus
    options:
      type: prometheus
      access: proxy
      url: "http://prometheus.local:9090"
```
