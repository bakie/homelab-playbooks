## Role variables

### medusa_group
The group for the medusa user

Default value is "medusa"

### medusa_user
The name of the medusa user

Default value is "medusa"

### medusa_user_home
The home directory of the medusa user

Default value is "/opt/medusa"

### medusa_repo
The repository of medusa

Default value is "https://github.com/pymedusa/Medusa.git"

### medusa_install_dir
The directory where medusa will be installed

Default value is "/opt/medusa"

### medusa_version
The version of medusa that needs to be installed

Default value is "master"

### medusa_url
The url which is used in the vhost.

Default value is "medusa.{{ top_lvl_domain }}"

###medusa_listen_port
The port on which medusa is listening which is used in the vhost for the proxying.

Default value is 8081
