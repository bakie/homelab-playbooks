# server.playbooks.komodo_periphery
Install and configure komodo_periphery agent on the remote hosts.

## Requirements
The [docker role](docker.md) is required for komodo periphery

## Role defaults
Available defaults are listed below, along with default value (see [defaults/main.yml](../roles/komodo_periphery/defaults/main.yml))
```yaml
komodo_periphery_user: "komodo"
komodo_periphery_group: "komodo"
```
Sets the user and group for all komodo periphery files and directories. Also sets the user and group that the komodo periphery process is executed as.

```yaml
komodo_periphery_base_path: "/opt/komodo"
komodo_periphery_install_path: "{{ komodo_periphery_base_path }}/bin"
komodo_periphery_config_path: "{{ komodo_periphery_base_path }}/config"
komodo_periphery_repo_path: "{{ komodo_periphery_base_path }}/repos"
komodo_periphery_stack_path: "{{ komodo_periphery_base_path }}/stacks"
komodo_periphery_build_path: "{{ komodo_periphery_base_path }}/builds"
```
The locations for all the directories and files required for komodo periphery.

```yaml
komodo_periphery_version: "v1.18.4"
```
Komodo periphery version that should be installed.

```yaml
komodo_periphery_listen_port: 8120
```
The port on which komodo periphery will listen.

```yaml
komodo_periphery_api_allowed_ips: []
```
Limit the ip addresses which can call the periphery api.

```yaml
komodo_periphery_api_passkeys: []
```
Require callers to provide one of the provided passkeys to access the periphery api.

## Role variables
Available variables are listed below, along with default value (see [vars/main.yml](../roles/komodo_periphery/vars/main.yml))
```yaml
komodo_periphery_download_url: "https://github.com/moghtech/komodo/releases/download/{{ komodo_periphery_version }}/periphery-x86_64"
```
The download url for the komodo periphery agent.
