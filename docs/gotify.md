# server.playbooks.gotify
Install and configure [gotify](https://gotify.net/) on the remote hosts.

## Role defaults
| Variable                     | Default                               | Comments |
|------------------------------|---------------------------------------|----------|
| gotify_default_user          | "admin"                               |          |
| gotify_default_user_password | "gotify"                              |          |
| gotify_user                  | "gotify"                              | The user which will run the gotify service  |
| gotify_group                 | "gotify"                              | The group which will run the gotify service |
| gotify_install_path          | "/opt/gotify"                         |          |
| gotify_config_path           | "/etc/gotify"                         |          |
| gotify_config_file_path      | "{{ gotify_config_path }}/config.yml" |          |
| gotify_version               | "2.5.0"                               |          |
| gotify_version_file_path     | "{{ gotify_install_path }}/version"   | version file is used to see if we need to update a previously installed gotify version |
| gotify_download_url          | "https://github.com/gotify/server/releases/download/v{{ gotify_version }}/gotify-linux-{{ deb_architecture.stdout }}.zip" |         |
| gotify_listen_port           | "9090"                                |          |