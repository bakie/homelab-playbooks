# server.playbooks.resolvconf
Install and configure resolvconf to the remote hosts. resolvconf will make sure the nameserver is added to the /etc/resolv.conf file

## Requirements
None

## Role defaults
Available defaults are listed below, along with default value (see [defaults/main.yml](../roles/resolvconf/defaults/main.yml))
```yaml
resolvconf_dns_resolver_ip: 10.1.1.1
```
the IP address of the dns resolver that gets set as the nameserver on the remote hosts in the file `/etc/resolvconf/resolv.conf.d/head`.

## Role variables
Available variables are listed below, along with default value (see [vars/main.yml](../roles/resolvconf/vars/main.yml))
```yaml
resolvconf_required_packages: [ "apt-utils" ]
```
A list of required packages that need to be installed with resolvconf.