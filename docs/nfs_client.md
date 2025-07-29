# server.playbooks.nfs_client
Install and configure nfs imports on the remote hosts.

## Requirements
None

## Role defaults
Available defaults are listed below, along with default value (see [defaults/main.yml](../roles/nfs_client/defaults/main.yml))
```yaml
nfs_client_imports: []
# nfs_client_imports:
#   - local_dir: "/media/dir"
#     remote_dir: "/home/user/dir"
#     nfs_server: 10.1.1.1
#     state: mounted
```
A list of nfs imports. nfs_server and remote_dir make up the src part, which will be mounted on local_dir. State can be absent, mounted, present, unmounted and remounted. Defaults to mounted.
