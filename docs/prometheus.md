# server.playbooks.prometheus
Install and configure prometheus on the remote hosts.

## Requirements
none

## Role variables
| Variable                     | Default           | Comments                                                                                                                                                                                                            |
|------------------------------|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| prometheus_group             | "prometheus"      |                                                                                                                                                                                                                     |
| prometheus_user              | "prometheus"      |                                                                                                                                                                                                                     |
| prometheus_home              | "/opt/prometheus" |                                                                                                                                                                                                                     |
| prometheus_storage_retention | "30d"             |                                                                                                                                                                                                                     |
| prometheus_blackbox_targets  | []                | example: <pre>- url: "duckduckgo.com"<br>  job: "blackbox"<br>- url: "airvpn.org"<br>  job: "blackbox"</pre>                                                                                                        |
| prometheus_alerting_rules    | []                | example: <pre>- group_name: applications<br>  rules:<br>    - name: "application"<br>      expr: "probe_success{job=\"blackbox\"} == 0"<br>      severity: "critical"<br>      summary: "Application is down"</pre> |
