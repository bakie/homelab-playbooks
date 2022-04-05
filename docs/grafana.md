# server.playbooks.grafana
Install and configure agrafana on the remote hosts.

## Requirements
None

## Role variables
| Variable               | Default                        | Comments |
|------------------------|--------------------------------|----------|
| grafana_url            | "grafana.{{ top_lvl_domain }}" |          |
| grafana_admin_user     | "grafana"                      |          |
| grafana_admin_password | "grafana"                      |          |
