# server.playbooks.sabnzbd
Install and configure sabnzbd on the remote hosts.

## Requirements
None

## Role defaults
Available defaults are listed below, along with default value (see [defaults/main.yml](../roles/sabnzbd/defaults/main.yml))
```yaml
sabnzbd_user: "sabnzbd"
sabnzbd_group: "sabnzbd"
```
Sets the user and group for all sabnzbd and directories. Also sets the user and group that the sabnzbd process is executed as.

```yaml
sabnzbd_install_path: "/opt/sabnzbd"
sabnzbd_required_paths:
  - "{{ sabnzbd_install_path }}/.sabnzbd"
  - "{{ sabnzbd_install_path }}/incomplete"
  - "{{ sabnzbd_install_path }}/complete"
  - "{{ sabnzbd_install_path }}/complete/tv"
  - "{{ sabnzbd_install_path }}/complete/movies"
  - "{{ sabnzbd_install_path }}/complete/music"
  - "{{ sabnzbd_install_path }}/nzb"
```
The locations for all the directories and files required for sabnzbd.

```yaml
sabnzbd_host: 0.0.0.0
sabnzbd_listen_port: 8080
```
The port and address on which sabnzbd will listen.

```yaml
sabnzbd_url: "sabnzbd.local.dev"
```
The url used to access sabnzbd from a web browser.
