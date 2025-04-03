# server.playbooks.vikunja
Install and configure vikunja on the remote hosts.

## Requirements
None

## Role defaults
Available defaults are listed below, along with default value (see [defaults/main.yml](../roles/vikunja/defaults/main.yml))
```yaml
vikunja_user: "vikunja"
vikunja_group: "vikunja"
```
Sets the user and group for all vikunja files and directories. Also sets the user and group that the vikunja process is executed as.

```yaml
vikunja_install_path: "/opt/vikunja"
vikunja_config_file_path: "/etc/vikunja/config.yml"
```
The locations for all the directories and files required for vikunja.

```yaml
vikunja_version: 0.24.6
```
Vikunja version that should be installed.

```yaml
vikunja_listen_port: 8080
vikunja_listen_address: "127.0.0.1"
```
The port and address on which the vikunja service is listening.

```yaml
vikunja_timezone: "GMT"
```
The timezone where the Vikunja service is running.

```yaml
vikunja_config:
  - { regexp: '^  interface:', line: '  interface: "{{ vikunja_listen_address }}:{{ vikunja_listen_port }}"' }
  - { regexp: '^  timezone:', line: '  timezone: {{ vikunja_timezone }}' }
```
Vikunja config settings that get configured in `{{ vikunja_config_file_path }}`.

## Role variables
Available variables are listed below, along with default value (see [vars/main.yml](../roles/vikunja/vars/main.yml))
```yaml
vikunja_download_url: "https://dl.vikunja.io/vikunja/{{ vikunja_version }}/vikunja-{{ vikunja_version }}-amd64.deb"
```
The download url for the vikunja service.