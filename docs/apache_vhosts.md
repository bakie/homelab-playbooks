# server.playbooks.apache
Configure apache vhosts on the remote hosts.

## Requirements
None

## Role variables
| Variable               | Default | Comments                                                                |
|------------------------|---------|-------------------------------------------------------------------------|
| required_apache_vhosts | []      | A list of apache vhosts which need to be configured on the remote host. |