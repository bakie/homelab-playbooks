# server.playbooks.prometheus
Install and configure prometheus on the remote hosts.

## Requirements
None

## Role variables
| Variable                             | Default           | Comments                                                                                                                                                                                                            |
|--------------------------------------|-------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| prometheus_blackbox_exporter_targets | []                | example: <pre>- url: "duckduckgo.com"<br>  job: "blackbox"<br>- url: "airvpn.org"<br>  job: "blackbox"</pre>                                                                                                        |
