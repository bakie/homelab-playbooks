# server.playbooks.nfs_client
Install and configure nfs imports on the remote hosts.

## Requirements
None

## Role variables
| Variable           | Default | Comments                                                                                                                                                     |
|--------------------|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| nfs_client_imports | []      | example: <pre>nfs_client_imports:<br>  - local_dir: "/media/dir"<br>    remote_dir: "/home/user/dir"<br>    nfs_server: 10.1.1.1<br>    state: mounted</pre> |
