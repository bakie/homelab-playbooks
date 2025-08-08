# server.playbooks.docker
Install and configure docker on the remote hosts.

## Requirements
None

## Role defaults
Available defaults are listed below, along with default value (see [defaults/main.yml](../roles/docker/defaults/main.yml))

## Role variables
Available variables are listed below, along with default value (see [vars/main.yml](../roles/docker/vars/main.yml))
```yaml
docker_required_packages: [ "ca-certificates", "curl", "gpg" ]
```
A list of required packages for installing and running docker.

```yaml
docker_apt_key_url: "https://download.docker.com/linux/debian/gpg"
docker_apt_repo_url: "deb [arch={{ deb_architecture.stdout }}] https://download.docker.com/linux/debian {{ version_codename.stdout }} stable"
```
The apt key url and apt repo url from which we will install docker.
