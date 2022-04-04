#!/usr/bin/env bash
#
# Description: Check if all dirs defined in /etc/fstab are actually mountpoints

if (( $# > 0 )); then
  >&2 echo "No arguments are required."
  exit 1
fi

echo "# HELP node_directory_mountpoint whether the dir is a mountpoint or not"
echo "# TYPE node_directory_mountpoint gauge"

FSTAB_DIRECTORIES=`cat /etc/fstab | awk '{print $2}' | grep -v 'swap'`

for FSTAB_DIR in $FSTAB_DIRECTORIES
do
  /bin/mountpoint $FSTAB_DIR -q
  # Return code 0 means that it is a mountpoint
  if [ $? -eq 0 ]; then
    echo "node_directory_fstab_mount{directory=\"$FSTAB_DIR\"} 1"
  else
    echo "node_directory_fstab_mount{directory=\"$FSTAB_DIR\"} 0"
  fi
done
