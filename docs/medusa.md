# server.playbooks.medusa
Install and configure medusa on the remote hosts.

## Requirements
None

## Role variables

| Variable                 | Default                                                                       | Comments |
|--------------------------|-------------------------------------------------------------------------------|----------|
| medusa_user              | "medusa"                                                                      |          |
| medusa_group             | "medusa"                                                                      |          |
| medusa_install_path      | "/opt/medusa"                                                                 |          |
| medusa_required_packages | [ "git-core", "python3", "mediainfo", "unrar-free", "openssl", "libssl-dev" ] |          |
| medusa_repo_url          | "https://github.com/pymedusa/Medusa.git"                                      |          |
| medusa_version           | "master"                                                                      |          |
| medusa_listen_port       | 8081                                                                          |          |