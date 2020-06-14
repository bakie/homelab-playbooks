# Role variables

### nfs_exports
The directories that will be made available to clients. Are added to /etc/exports

Example:
```yaml
nfs_exports:
  - /home/dir1 host1.local(rw,sync,no_root_squash,no_subtree_check)
  - /home/dir2/dir host2.local(rw,sync,no_root_squash,no_subtree_check)
  - /home/dir1/test host3.local(rw,sync,no_root_squash,no_subtree_check)
```

Default value is []