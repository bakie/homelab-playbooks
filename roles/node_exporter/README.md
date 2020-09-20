# Role variables

### node_exporter_group
The group for the node_exporter user

Default value is "node_exporter"

### node_exporter_user
The name of the node_exporter user

Default value is "node_exporter"

### node_exporter_version
The version of the node exporter

Default value is "1.0.1"

### node_exporter_home
The home dir of the node_exporter user

Default value is "/opt/node_exporter"

### node_exporter_config_path
The path for the configurations required for node_exporter

Default value is "/etc/node_exporter/config"

### node_exporter_web_listen_port
The port on which node_exporter should listen

Default value is 9100

### node_exporter_web_listen_address
The address on which node_exporter should listen

Default value is "0.0.0.0:{{ node_exporter_web_listen_port }}"

### node_exporter_enabled_collectors
The collectors which need to be enabled

Default value is
```
```

### node_exporter_disabled_collectors
The collectors which need to be disabled

Default value is []
