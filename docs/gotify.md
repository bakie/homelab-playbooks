# server.playbooks.gotify
Install and configure [gotify](https://gotify.net/) on the remote hosts.

## Requirements
None

## Role defaults
Available defaults are listed below, along with default value (see [defaults/main.yml](../roles/gotify/defaults/main.yml))
```yaml
gotify_default_user: "admin"
gotify_default_user_password: "gotify"
```
The default login user and password

```yaml
gotify_user: "gotify"
gotify_group: "gotify"
```
Sets the user and group for all gotify files and directories. Also sets the user and group that the gotify process is executed as.

```yaml
gotify_install_path: "/opt/gotify"
gotify_config_path: "/etc/gotify"
gotify_config_file_path: "{{ gotify_config_path }}/config.yml"
```
Specify the locations for all the directories and files required for gotify.

```yaml
gotify_version: "2.5.0"                               |          |
```
Gotify version that should be installed.

```yaml
gotify_version_file_path: "{{ gotify_install_path }}/version"
```
The location of the version file. The version file is used to see if we need to update a previously installed gotify version.

```yaml
gotify_listen_port: "9090"
```
The port on which gotify will listen.

## Role variables
Available variables are listed below, along with default value (see [vars/main.yml](../roles/gotify/vars/main.yml))
```yaml
gotify_download_url: "https://github.com/gotify/server/releases/download/v{{ gotify_version }}/gotify-linux-{{ deb_architecture.stdout }}.zip"
```
The download url from which to download gotify.
