# server.playbooks.nfs_server
Install and configure nfs exports on the remote hosts.

## Requirements
None

## Role variables
| Variable           | Default | Comments                                                                                                                                                                                                                                                       |
|--------------------|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| nfs_server_exports | []      | example: <pre>nfs_exports:<br>  - /home/dir1 host1.local(rw,sync,no_root_squash,no_subtree_check)<br>  - /home/dir2/dir host2.local(rw,sync,no_root_squash,no_subtree_check)<br>  - /home/dir1/test host3.local(rw,sync,no_root_squash,no_subtree_check)</pre> |
