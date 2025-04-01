# server.playbooks.miniflux
Install and configure miniflux on the remote hosts.

## Requirements
None

## Role defaults
Available defaults are listed below, along with default value (see [defaults/main.yml](../roles/miniflux/defaults/main.yml))
```yaml
miniflux_db_name: "miniflux"
miniflux_db_user: "miniflux"
miniflux_db_password: "miniflux"
```
Database settings for running Miniflux.

```yaml
miniflux_url: "miniflux.local.dev"
miniflux_listen_port: 8080
```
The url used to access Miniflux from a web browser and on which port Miniflux will listen.

## Role variables
Available variables are listed below, along with default value (see [vars/main.yml](../roles/miniflux/vars/main.yml))
```yaml
miniflux_required_packages: [ "postgresql-15", "python3-psycopg2" ]
```
A list of required packages for installing and running Miniflux.
