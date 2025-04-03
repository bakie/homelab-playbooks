# homelab.playbooks.apaache
Install and configures apache on the remote hosts.

## Requirements
None

## Role defaults
Available defaults are listed below, along with default value (see [defaults/main.yml](../roles/apache/defaults/main.yml))
```yaml
apache_required_packages: [ "python3-passlib" ]
```
A list of required packages that need to be installed with apache2.

```yaml
apache_modules: 
  - autoindex
  - deflate
  - expires
  - filter
  - headers
  - http2
  - include
  - mime
  - rewrite
  - setenvif
  - ssl
  - proxy_html
  - proxy_http
  - proxy_wstunnel
  - xml2enc
```
A list of apache modules that need to be enabled.

```yaml
apache_security_config:
  - { regexp: '^ServerTokens', line: 'ServerTokens Prod' }
  - { regexp: '^ServerSignature', line: 'ServerSignature Off' }
```
Security settings that get configured in the file `/etc/apache2/conf-available/security.conf`.

```yaml
apache_ssl_config:
  - { regexp: '^SSLCipherSuite', line: 'SSLCipherSuite HIGH:!aNULL:!SHA1' }
```
Ssl config settings that get configured in the file `/etc/apache2/mods-available/ssl.conf`.

```yaml
apache_hostname_config:
  - { regexp: '^ServerName', line: 'ServerName {{ ansible_hostname }}' }
```
Settings that get configured in the file `/etc/apache2/conf-available/hostname.conf`.

```yaml
apache_listen_ports_config:
  - { regexp: 'Listen 80', replace: 'Listen 0.0.0.0:80' }
  - { regexp: 'Listen 443', replace: 'Listen 0.0.0.0:443' }
```
listen port settings that get configured in the file `/etc/apache2/ports.conf`.
