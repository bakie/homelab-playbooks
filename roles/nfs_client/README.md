## Role Variables

### nfs_imports
The mounts that are going to be added to fstab.
The local_dir, remote_dir and nfs_server are required. The state value defaults to mounted.

Example:
```
nfs_imports:
  - local_dir: "/media/dir"
    remote_dir: "/home/user/dir"
    nfs_server: 10.1.1.1
    state: mounted
```

Default value is []
