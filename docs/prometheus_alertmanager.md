# server.playbooks.prometheus_alertmanager
Install and configure prometheus alertmanager on the remote hosts.

## Requirements
None

## Role variables
| Variable                              | Default                                        | Comments                                            |
|---------------------------------------|------------------------------------------------|-----------------------------------------------------|
| prometheus_alertmanager_slack_api_url | "http://prometheus_alertmanager_slack_api_url" | Slack api url where the alertmanager should post to |