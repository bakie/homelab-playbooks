# homelab.playbooks.base_setup
Install default packages on the remote hosts.

## Requirements
None

## Role defaults
Available defaults are listed below, along with default value (see [defaults/main.yml](../roles/base_setup/defaults/main.yml))
```yaml
base_setup_packages: [ "python3-apt", "aptitude", "curl", "htop", "rsync", "sudo", "vim", "build-essential", "acl", "cron" ]
```
A list of default packages to install on the remote host.
