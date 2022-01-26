# server.playbooks.node_exporter
Install and configure the prometheus node exporter on the remote hosts.

## Requirements
none

## Role variables
| Variable            | Default              | Comments |
|---------------------|----------------------|----------|
| node_exporter_user  | "node_exporter"      |          |
| node_exporter_group | "node_exporter"      |          |
| node_exporter_home  | "/opt/node_exporter" |          |
