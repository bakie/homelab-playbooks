# server.playbooks.transmission
Install and configure transmission on the remote hosts.

## Requirements
None

## Role defaults
Available defaults are listed below, along with default value (see [defaults/main.yml](../roles/transmission/defaults/main.yml))
```yaml
transmission_user: "transmission"
transmission_group: "transmission"
```
Sets the user and group for all transmission files and directories. Also sets the user and group that the sabnzbd process is executed as.

```yaml
transmission_install_path: "/opt/transmission"
transmission_required_paths:
  - "{{ transmission_install_path }}/completed"
  - "{{ transmission_install_path }}/incomplete"
  - "{{ transmission_install_path }}/torrents"
  - "{{ transmission_install_path }}/watchdir"
transmission_settings_file_path: "{{ transmission_install_path }}/.config/transmission-daemon/settings.json"
```
The locations for all the directories and files required for transmission.

```yaml
transmission_listen_port: 9091
```
The port on which transmission will listen.

```yaml
transmission_settings:
  - option: "\"download-queue-size\""
    value: 10
  - option: "\"rpc-username\""
    value: "\"transmission\""
  - option: "\"rpc-password\""
    value: "\"transmission\""
  - option: "\"alt-speed-down\""
    value: "500"
  - option: "\"alt-speed-up\""
    value: "1"
  - option: "\"download-dir\""
    value: "\"{{ transmission_install_path }}/completed\""
  - option: "\"encryption\""
    value: "2"
  - option: "\"incomplete-dir\""
    value: "\"{{ transmission_install_path }}/incomplete\""
  - option: "\"incomplete-dir-enabled\""
    value: "true"
  - option: "\"rpc-host-whitelist-enabled\""
    value: "false"
  - option: "\"rpc-whitelist-enabled\""
    value: "false"
  - option: "\"rpc-bind-address\""
    value: "\"127.0.0.1\""
```
A list of transmission settings that get configured in `{{ transmission_settings_file_path }}`.
