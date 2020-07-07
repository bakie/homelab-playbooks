# Role variables

### prometheus_node_exporter_group
The group for the prometheus_node_exporter user

Default value is "prometheus_node_exporter"

### prometheus_node_exporter_user
The name of the prometheus_node_exporter user

Default value is "prometheus_node_exporter"

### prometheus_node_exporter_version
The version of the node exporter

Default value is "1.0.1"

### prometheus_node_exporter_home
The home dir of the prometheus_node_exporter user

Default value is "/opt/prometheus_node_exporter"

### prometheus_node_exporter_config_path
The path for the configurations required for prometheus_node_exporter

Default value is "/opt/prometheus_node_exporter/config"

### prometheus_node_exporter_web_listen_port
The port on which prometheus_node_exporter should listen

Default value is 9100

### prometheus_node_exporter_web_listen_address
The address on which prometheus_node_exporter should listen

Default value is "0.0.0.0:{{ prometheus_node_exporter_web_listen_port }}"

### prometheus_node_exporter_enabled_collectors
The collectors which need to be enabled

Default value is
```
```

### prometheus_node_exporter_disabled_collectors
The collectors which need to be disabled

Default value is []
