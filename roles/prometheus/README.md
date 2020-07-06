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

### prometheus_configs_dir
The dir for the configurations required for prometheus

Default value is "/opt/prometheus/config"

### prometheus_web_listen_address
The address and port on which prometheus should listen

Default value is "0.0.0.0:9090"

### prometheus_storage_retention
The retention for the data

Default value is "30d"