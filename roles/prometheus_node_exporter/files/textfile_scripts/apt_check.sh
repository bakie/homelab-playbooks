#!/usr/bin/env bash
#
# Description: Expose metrics from apt-check.

APT_CHECK="$(/usr/lib/update-notifier/apt-check 2>&1)"
IFS=";"
APT_CHECK_ARRAY=($APT_CHECK)
echo "# HELP apt_updates_pending Apt package pending updates"
echo "# TYPE apt_updates_pending gauge"
echo "apt_updates_pending ${APT_CHECK_ARRAY[0]}"
echo "# HELP apt_security_updates_pending Apt package pending security updates"
echo "# TYPE apt_security_updates_pending gauge"
echo "apt_security_updates_pending ${APT_CHECK_ARRAY[1]}"
