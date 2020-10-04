# Role variables

### blackboxexporter_group
The group for the blackboxexporter user

Default value is "blackboxexporter"

### blackboxexporter_user
The name of the blackboxexporter user

Default value is "blackboxexporter"

### blackboxexporter_version
The version of the node exporter

Default value is "1.0.1"

### blackboxexporter_home
The home dir of the blackboxexporter user

Default value is "/opt/blackboxexporter"

### blackboxexporter_config_path
The path for the configurations required for blackboxexporter

Default value is "/etc/blackboxexporter"

### blackboxexporter_web_listen_port
The port on which blackboxexporter should listen

Default value is 9100

### blackboxexporter_web_listen_address
The address on which blackboxexporter should listen

Default value is "0.0.0.0:{{ blackboxexporter_web_listen_port }}"

### blackboxexporter_enabled_collectors
The collectors which need to be enabled

Default value is
```
```

### blackboxexporter_disabled_collectors
The collectors which need to be disabled

Default value is []
