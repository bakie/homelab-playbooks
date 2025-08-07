# Homelab-playbooks

Ansible roles for my homelab setup

## Roles
| Role                         | Build Status                                                                                                                                                                                                                                                                       | Documentation                                         |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| apache                       | [![Role: bakie.homelab.apache](https://github.com/bakie/homelab-playbooks/workflows/bakie.homelab.apache/badge.svg)](https://github.com/bakie/homelab-playbooks/actions?query=workflow%3Abakie.homelab.apache++)                                                                   | [Documentation](docs/apache.md)                       |
| apache_vhosts                | [![Role: bakie.homelab.apache_vhosts](https://github.com/bakie/homelab-playbooks/workflows/bakie.homelab.apache_vhosts/badge.svg)](https://github.com/bakie/homelab-playbooks/actions?query=workflow%3Abakie.homelab.apache_vhosts++)                                              | [Documentation](docs/apache_vhosts.md)                |
| apt                          | [![Role: bakie.homelab.apt](https://github.com/bakie/homelab-playbooks/workflows/bakie.homelab.apt/badge.svg)](https://github.com/bakie/homelab-playbooks/actions?query=workflow%3Abakie.homelab.apt++)                                                                            | [Documentation](docs/apt.md)                          |
| base_setup                   | [![Role: bakie.homelab.base_setup](https://github.com/bakie/homelab-playbooks/workflows/bakie.homelab.base_setup/badge.svg)](https://github.com/bakie/homelab-playbooks/actions?query=workflow%3Abakie.homelab.base_setup++)                                                       | [Documentation](docs/base_setup.md)                   |
| docker                       | [![Role: bakie.homelab.docker](https://github.com/bakie/homelab-playbooks/workflows/bakie.homelab.docker/badge.svg)](https://github.com/bakie/homelab-playbooks/actions?query=workflow%3Abakie.homelab.docker++)                                                       | [Documentation](docs/docker.md)                   |
| gotify                       | [![Role: bakie.homelab.gotify](https://github.com/bakie/homelab-playbooks/workflows/bakie.homelab.gotify/badge.svg)](https://github.com/bakie/homelab-playbooks/actions?query=workflow%3Abakie.homelab.gotify++)                                                                  | [Documentation](docs/gotify.md)                      |
| grafana                      | [![Role: bakie.homelab.grafana](https://github.com/bakie/homelab-playbooks/workflows/bakie.homelab.grafana/badge.svg)](https://github.com/bakie/homelab-playbooks/actions?query=workflow%3Abakie.homelab.grafana++)                                                                | [Documentation](docs/grafana.md)                      |
| komodo_core                  | [![Role: bakie.homelab.komodo_core](https://github.com/bakie/homelab-playbooks/workflows/bakie.homelab.komodo_core/badge.svg)](https://github.com/bakie/homelab-playbooks/actions?query=workflow%3Abakie.homelab.komodo_core++)                                                                | [Documentation](docs/komodo_core.md)                      |
| komodo_periphery             | [![Role: bakie.homelab.komodo_periphery](https://github.com/bakie/homelab-playbooks/workflows/bakie.homelab.komodo_periphery/badge.svg)](https://github.com/bakie/homelab-playbooks/actions?query=workflow%3Abakie.homelab.komodo_periphery++)                                                                | [Documentation](docs/komodo_periphery.md)                      |
| medusa                       | [![Role: bakie.homelab.medusa](https://github.com/bakie/homelab-playbooks/workflows/bakie.homelab.medusa/badge.svg)](https://github.com/bakie/homelab-playbooks/actions?query=workflow%3Abakie.homelab.medusa++)                                                                   | [Documentation](docs/medusa.md)                       |
| miniflux                     | [![Role: bakie.homelab.miniflux](https://github.com/bakie/homelab-playbooks/workflows/bakie.homelab.miniflux/badge.svg)](https://github.com/bakie/homelab-playbooks/actions?query=workflow%3Abakie.homelab.miniflux++)                                                                   | [Documentation](docs/miniflux.md)                       |
| nfs_client                   | [![Role: bakie.homelab.nfs_client](https://github.com/bakie/homelab-playbooks/workflows/bakie.homelab.nfs_client/badge.svg)](https://github.com/bakie/homelab-playbooks/actions?query=workflow%3Abakie.homelab.nfs_client++)                                                       | [Documentation](docs/nfs_client.md)                   |
| nfs_server                   | [![Role: bakie.homelab.nfs_server](https://github.com/bakie/homelab-playbooks/workflows/bakie.homelab.nfs_server/badge.svg)](https://github.com/bakie/homelab-playbooks/actions?query=workflow%3Abakie.homelab.nfs_server++)                                                       | [Documentation](docs/nfs_server.md)                   |
| openvpn                      | [![Role: bakie.homelab.openvpn](https://github.com/bakie/homelab-playbooks/workflows/bakie.homelab.openvpn/badge.svg)](https://github.com/bakie/homelab-playbooks/actions?query=workflow%3Abakie.homelab.openvpn++)                                                                | [Documentation](docs/openvpn.md)                      |
| prometheus                   | [![Role: bakie.homelab.prometheus](https://github.com/bakie/homelab-playbooks/workflows/bakie.homelab.prometheus/badge.svg)](https://github.com/bakie/homelab-playbooks/actions?query=workflow%3Abakie.homelab.prometheus++)                                                       | [Documentation](docs/prometheus.md)                   |
| prometheus_alertmanager      | [![Role: bakie.homelab.prometheus_alertmanager](https://github.com/bakie/homelab-playbooks/workflows/bakie.homelab.prometheus_alertmanager/badge.svg)](https://github.com/bakie/homelab-playbooks/actions?query=workflow%3Abakie.homelab.prometheus_alertmanager++)                | [Documentation](docs/prometheus_alertmanager.md)      |
| prometheus_blackbox_exporter | [![Role: bakie.homelab.prometheus_blackbox_exporter](https://github.com/bakie/homelab-playbooks/workflows/bakie.homelab.prometheus_blackbox_exporter/badge.svg)](https://github.com/bakie/homelab-playbooks/actions?query=workflow%3Abakie.homelab.prometheus_blackbox_exporter++) | [Documentation](docs/prometheus_blackbox_exporter.md) |
| prometheus_node_exporter     | [![Role: bakie.homelab.prometheus_node_exporter](https://github.com/bakie/homelab-playbooks/workflows/bakie.homelab.prometheus_node_exporter/badge.svg)](https://github.com/bakie/homelab-playbooks/actions?query=workflow%3Abakie.homelab.prometheus_node_exporter++)             | [Documentation](docs/prometheus_node_exporter.md)     |
| resolvconf                   | [![Role: bakie.homelab.resolvconf](https://github.com/bakie/homelab-playbooks/workflows/bakie.homelab.resolvconf/badge.svg)](https://github.com/bakie/homelab-playbooks/actions?query=workflow%3Abakie.homelab.resolvconf++)                                                       | [Documentation](docs/resolvconf.md)                   |
| sabnzbd                      | [![Role: bakie.homelab.sabnzbd](https://github.com/bakie/homelab-playbooks/workflows/bakie.homelab.sabnzbd/badge.svg)](https://github.com/bakie/homelab-playbooks/actions?query=workflow%3Abakie.homelab.sabnzbd++)                                                                | [Documentation](docs/sabnzbd.md)                      |
| ssl_cert                     | [![Role: bakie.homelab.ssl_cert](https://github.com/bakie/homelab-playbooks/workflows/bakie.homelab.ssl_cert/badge.svg)](https://github.com/bakie/homelab-playbooks/actions?query=workflow%3Abakie.homelab.ssl_cert++)                                                             | [Documentation](docs/ssl_cert.md)                     |
| transmission                 | [![Role: bakie.homelab.transmission](https://github.com/bakie/homelab-playbooks/workflows/bakie.homelab.transmission/badge.svg)](https://github.com/bakie/homelab-playbooks/actions?query=workflow%3Abakie.homelab.transmission++)                                                 | [Documentation](docs/transmission.md)                 |
| vikunja                      | [![Role: bakie.homelab.vikunja](https://github.com/bakie/homelab-playbooks/workflows/bakie.homelab.vikunja/badge.svg)](https://github.com/bakie/homelab-playbooks/actions?query=workflow%3Abakie.homelab.vikunja++)                                                 | [Documentation](docs/vikunja.md)                                     |

# Poetry and pyenv
[poetry](https://github.com/python-poetry/poetry) and [pyenv](https://github.com/pyenv/pyenv) is required for running the playbooks.
pyenv lets you install multiple versions of python and Poetry is a dependency management tool for python.

## Getting started
### Install correct python version
There is a file .python-version which contains the python version required to run everything. To install that version using pyenv just run the following command:
```
pyenv install
```
This will install the python version specified in the .python-version file.

### Install dependencies
The following commands will switch you to the virtual env and will install all required packages listed in the poetry.lock file.
```
poetry env use $(cat .python-version)
eval $(poetry env activate)
poetry install
```

When this is done you will have ansible installed in the virtual env and are ready to start using it.

## Testing
### Running tests locally
We use molecule for testing and pytest-testinfra to run the actual python written tests.

To run the tests for a specific role, execute the following command
```
molecule test -s apache
```
This will spin up the required docker images and run ansible against those. The -s option is to specify which "role" to test.

There are different scenario's available when using molecule.
```
create
check
converge
destroy
test
...
```
The exact details of these can be found in the .config/molecule/config.yml file.

When you create a new role or make changes to an existing role and need to test it quickly you can use the converge scenario
```
molecule converge -s apache
```
This will only do a lint check, create the docker instances, run the converge.yml playbook and the idempotence test.
Once you have finished the role or the changes run the complete test scenario to make sure all the tests still pass.

### Handy test check
You can use the host.system_info to test for different things on different distribtions/releases
```
if host.system_info.distribution == "ubuntu" and host.system_info.release < "18.04":
    assert $something_on_ubuntu_18.04
```

### Expose ports for local testing
Sometimes you need to expose the port to your localhost for testing. Add the published_ports to the platforms config.
```
  - name: debian-bookworm-${MOLECULE_SCENARIO_NAME:-instance}
    image: debian:bookworm
    privileged: true
    pre_build_image: false
    command: "/lib/systemd/systemd"
    volumes:
      - "/sys/fs/cgroup:/sys/fs/cgroup:rw"
    cgroupns_mode: host
    published_ports:
      - 9090:8080
```
This exposes the port 8080 to your localhost port 9090, and then you can access it via localhost:9090

### Tests using github actions
To make sure we test everything when it is pushed we use github actions. Each role has its own workflow. The reason is that we only run the specific workflow and test only the role that has changed files.
In github actions you can specify the paths of the files that trigger the workflow. And as such we don't need to test all roles if only one role has been changed. That is because role X should not depend on role Y and vice versa and should not break.
