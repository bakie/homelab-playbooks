# Role variables

### prometheus_group
The group for the prometheus user

Default value is "prometheus"

### prometheus_user
The name of the prometheus user

Default value is "prometheus"

### prometheus_home
The home dir of the prometheus user

Default value is "/opt/prometheus"

### prometheus_config_path
The path for the configurations required for prometheus

Default value is "/opt/prometheus/config"

### prometheus_web_listen_port
The port on which prometheus should listen

Default value is 9090

### prometheus_web_listen_address
The address on which prometheus should listen

Default value is "0.0.0.0:{{ prometheus_web_listen_port }}"

### prometheus_storage_retention
The retention for the data

Default value is "30d"