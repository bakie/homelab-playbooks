# server.playbooks.medusa
Install and configure medusa on the remote hosts.

## Requirements
none

## Role variables
| Variable         | Default                       | Comments |
|------------------|-------------------------------|----------|
| medusa_group     | "medusa"                      |          | 
| medusa_user      | "medusa"                      |          | 
| medusa_user_home | "/opt/medusa"                 |          | 
| medusa_url       | "medusa.{{ top_lvl_domain }}" |          | 
