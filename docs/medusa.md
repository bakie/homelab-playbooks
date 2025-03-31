# server.playbooks.medusa
Install and configure medusa on the remote hosts.

## Requirements
None

## Role defaults
Available defaults are listed below, along with default value (see [defaults/main.yml](../roles/medusa/defaults/main.yml))
```yaml
medusa_user: "medusa"
medusa_group: "medusa"
```
Sets the user and group for all medusa files and directories. Also sets the user and group that the medusa process is executed as.

```yaml
medusa_install_path: "/opt/medusa"
```
The installtion path for medusa.

```yaml
medusa_version: "master"
```
Medusa version that should be installed.

```yaml
medusa_listen_port: 8081
```
The port on which medusa will listen.

## Role variables
Available variables are listed below, along with default value (see [vars/main.yml](../roles/medusa/vars/main.yml))
```yaml
medusa_required_packages: [ "git-core", "python3", "mediainfo", "unrar-free", "openssl", "libssl-dev" ]
```
A list of required packages for installing and running Medusa.

```yaml
medusa_repo_url: "https://github.com/pymedusa/Medusa.git"
```
The repo url from which to download Medusa.
