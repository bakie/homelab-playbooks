# server.playbooks.transmission
Install and configure transmission on the remote hosts.

## Requirements
none

## Role variables
| Variable                                     | Default                                       | Comments |
|----------------------------------------------|-----------------------------------------------|----------|
| transmission_group                           | "debian-transmission"                         |          |
| transmission_user                            | "debian-transmission"                         |          |
| transmission_user_home                       | "/opt/transmission"                           |          |
| transmission_rpc_username                    | "\"transmission\""                            |          |
| transmission_rpc_password                    | "\"transmission\""                            |          |
| transmission_settings_alt_speed_down         | 500                                           |          |
| transmission_settings_alt_speed_up           | 1                                             |          |
| transmission_settings_download_dir           | "\"{{ transmission_user_home }}/completed\""  |          |
| transmission_settings_encryption             | 2                                             |          |
| transmission_settings_incomplete_dir         | "\"{{ transmission_user_home }}/incomplete\"" |          |
| transmission_settings_incomplete_dir_enabled | "true"                                        |          |
| transmission_rpc_host_whitelist_enabled      | "false"                                       |          |
| transmission_rpc_whitelist_enabled           | "false"                                       |          |
