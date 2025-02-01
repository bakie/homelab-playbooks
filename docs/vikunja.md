# server.playbooks.vikunja
Install and configure vikunja on the remote hosts.

## Requirements
None

## Role variables
| Variable               | Default     | Comments |
|------------------------|-------------|----------|
| vikunja_listen_port    | 8080        |          |
| vikunja_listen_address | "127.0.0.1" |          |
| vikunja_group          | "vikunja"   |          |
| vikunja_user           | "vikunja"   |          |
| vikunja_timezone       | "GMT"       |          |
| vikunja_config         |  <pre>- { regexp: '^  interface:', line: '  interface: "{{ vikunja_listen_address }}:{{ vikunja_listen_port }}"' }<br>- { regexp: '^  timezone:', line: '  timezone: {{ vikunja_timezone }}' }</pre>|   |
