# server.playbooks.prometheus_alertmanager
Install and configure prometheus alertmanager on the remote hosts.

## Requirements
none

## Role variables
| Variable                      | Default                        | Comments |
|-------------------------------|--------------------------------|----------|
| prometheus_alertmanager_group | "alertmanager"                 |          |
| prometheus_alertmanager_user  | "alertmanager"                 |          |
| prometheus_alertmanager_home  | "/opt/prometheus_alertmanager" |          |
