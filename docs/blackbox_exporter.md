# homelab.playbooks.blackbox_exporter
Install and configures [blackbox_exporter](https://github.com/prometheus/blackbox_exporter) on the remote hosts.

The blackbox exporter allows blackbox probing of endpoints over HTTP, HTTPS, DNS, TCP and ICMP.

## Requirements
None

## Role variables
| Variable                             | Default                                           | Comments |
|--------------------------------------|---------------------------------------------------|----------|
| blackbox_exporter_user               | "blackbox_exporter"                               |          |
| blackbox_exporter_group              | "blackbox_exporter"                               |          |
| blackbox_exporter_home               | "/opt/blackbox_exporter"                          |          |
| blackbox_exporter_version            | 0.17.0                                            |          |
| blackbox_exporter_web_listen_port    | "9101"                                            |          |
| blackbox_exporter_web_listen_address | "0.0.0.0:{{ blackbox_exporter_web_listen_port }}" |          |