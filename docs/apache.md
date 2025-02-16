# homelab.playbooks.apaache
Install and configures apache on the remote hosts.

## Requirements
None

## Role defaults
| Variable                 | Value                 | Comments                                                                |
|--------------------------|-----------------------|-------------------------------------------------------------------------|
| apache_required_packages | [ "python3-passlib" ] | List of required packages that need to be installed with apache2        |
| apache_modules | <pre>- autoindex<br>- deflate<br>- expires<br>- filter<br>- headers<br>- http2<br>- include<br>- mime<br>- rewrite<br>- setenvif<br>- ssl<br>- proxy_html<br>- proxy_http<br>- proxy_wstunnel<br>- xml2enc</pre> | A list of apache modules that need to be enabled. |
| apache_security_config   | <pre>- { regexp: '^ServerTokens', line: 'ServerTokens Prod' }<br>- { regexp: '^ServerSignature', line: 'ServerSignature Off' }</pre> | Settings that get configured in the file `/etc/apache2/conf-available/security.conf` |
| apache_ssl_config | <pre>- { regexp: '^SSLCipherSuite', line: 'SSLCipherSuite HIGH:!aNULL:!SHA1' }</pre> | Settings that get configured in the file `/etc/apache2/mods-available/ssl.conf` |
| apache_hostname_config | <pre>- { regexp: '^ServerName', line: 'ServerName {{ ansible_hostname }}' }</pre> | Settings that get configured in the file `/etc/apache2/conf-available/hostname.conf` |
| apache_listen_ports_config | <pre>- { regexp: 'Listen 80', replace: 'Listen 0.0.0.0:80' }<br>- { regexp: 'Listen 443', replace: 'Listen 0.0.0.0:443' } | Settings that get configured in the file `/etc/apache2/ports.conf` |
