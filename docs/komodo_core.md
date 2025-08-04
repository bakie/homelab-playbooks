# server.playbooks.komodo_core
Install and configure komodo_core on the remote hosts.

## Requirements
The [docker role](docker.md) is required for running komodo core

## Role defaults
Available defaults are listed below, along with default value (see [defaults/main.yml](../roles/komodo_core/defaults/main.yml))
```yaml
komodo_core_user: "komodo_core"
komodo_core_group: "komodo_core"
```
The name and password of the komodo_core user running the docker containers. 

```yaml
komodo_core_install_path: "/opt/komodo"
```
The path where we install the komodo core docker file and env file.

```yaml
komodo_core_version: "1.18"
komodo_core_ferretdb_version: "2.4.0"
komodo_core_postgres_documentdb_version: "16-0.105.0-ferretdb-2.4.0"
```
komodo_core, ferretdb and postgres documentdb version that should be installed via the docker compose file.

```yaml
komodo_core_db_user: "admin"
komodo_core_db_password: "admin"
```
Database settings for running komodo core.

## Role variables
None
