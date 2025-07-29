# server.playbooks.nfs_server
Install and configure nfs exports on the remote hosts.

## Requirements
None

## Role defaults
Available defaults are listed below, along with default value (see [defaults/main.yml](../roles/nfs_server/defaults/main.yml))
```yaml
nfs_server_exports: []
# nfs_server_exports:
#   - /home/dir1 remote_host1.local(rw,sync,no_root_squash,no_subtree_check)
#   - /home/dir2/dir remote_host2.local(rw,sync,no_root_squash,no_subtree_check)
#   - /home/dir1/test remote_host3.local(rw,sync,no_root_squash,no_subtree_check)
```
A list of nfs_server_exports. This list will be places in the `/etc/exports` file. The file controls which file systems are exported to remote hosts and specifies options.
