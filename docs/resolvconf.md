# server.playbooks.resolvconf
Install and configure resolvconf to the remote hosts. resolvconf will make sure the nameserver is added to the /etc/resolv.conf file

## Requirements
none

## Role variables
| Variable                   | Default  | Comments                           |
|----------------------------|----------|------------------------------------|
| resolvconf_dns_resolver_ip | 10.1.1.1 | the IP address of the dns resolver |
