# server.playbooks.miniflux
Install and configure miniflux on the remote hosts.

## Requirements
None

## Role variables

| Variable                   | Default                                 | Comments |
|----------------------------|-----------------------------------------|----------|
| miniflux_url               | "miniflux.local.dev"                    |          |
| miniflux_listen_port       | 8080                                    |          |
| miniflux_db_name           | "miniflux"                              |          |
| miniflux_db_user           | "miniflux"                              |          |
| miniflux_db_password       | "miniflux"                              |          |
| miniflux_required_packages | [ "postgresql-15", "python3-psycopg2" ] |          |