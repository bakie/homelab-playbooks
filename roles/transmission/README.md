# Role variables

### transmission_group
The group for the transmission user

Default value is "transmission"

### transmission_user
The name of the transmission user

Default value is "transmission"

### transmission_user_home
The home directory of the transmission user

Default value is "/opt/transmission"

### transmission_settings_file
The location of the transmission settings file

Default value is "{{ transmission_user_home }}/.config/transmission-daemon/settings.json"

### transmission_url
The url which is used in the vhost.

Default value is "transmission.{{ top_lvl_domain }}"

###transmission_listen_port
The port on which transmission is listening which is used in the vhost for the proxying.

Default value is 9091


## Next settings are for the settings file
### transmission_rpc_username
The username when logging in to transmission

Default value is "transmission"

### transmission_rpc_password
The password when logging in to transmission

Default value is "transmission"

### transmission_settings_alt_speed_down
The max download speed

Default value is 500

### transmission_settings_alt_speed_up
The max upload speed

Default value is 1

### transmission_settings_download_dir
The location of the download dir

Default value is "\\"{{ transmission_user_home }}/completed\\""

### transmission_settings_encryption
The lvl of encryption

Default value is 2

### transmission_settings_incomplete_dir
The location of the incomplete dir

Default value is "\\"{{ transmission_user_home }}/incomplete\\""

### transmission_settings_incomplete_dir_enabled
Setting to enable or disable the use of the incomplete_dir

Default value is "true"

### transmission_settings
Combines all of the above settings into option value

Default value is

```
transmission_settings:
     - option: "\"alt-speed-down\""
       value: "{{ alt_speed_down }}"
     - option: "\"alt-speed-up\""
       value: "{{ alt_speed_up }}"
     - option: "\"download-dir\""
       value: "{{ download_dir }}"
     - option: "\"encryption\""
       value: "{{ encryption }}"
     - option: "\"incomplete-dir\""
       value: "{{ incomplete_dir }}"
     - option: "\"incomplete-dir-enabled\""
       value: "{{ incomplete_dir_enabled }}"
```
