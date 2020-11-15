# Role variables

### pihole_group
The group for the pihole user

Default value is "pihole"

### pihole_user
The name of the pihole user

Default value is "pihole"

### pihole_config_path
The path for the configurations required for pihole

Default value is "/etc/pihole"

### pihole_custom_dns_entries
A dictionary containing the custom dns entries.

Example:
```
pihole_custom_dns_entries:
  - ip: 10.1.1.100
    url: pihole.custom.dns
  - ip: 10.1.1.83
    url: pihole_test.custom.dns
```

Default value is []

### pihole_automatic_update
Automatically update pihole to the latest version.
If set to false if will not update pihole to the latest version once intalled.

Default value is true
