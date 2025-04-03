# server.playbooks.ssl_cert
Install and configure ssl_cert on the remote hosts.

## Requirements
None

## Role defaults
Available defaults are listed below, along with default value (see [defaults/main.yml](../roles/ssl_cert/defaults/main.yml))
```yaml
ssl_group: "ssl-cert"
```
The group for the created ssl dir and ssl files. The owner of the ssl dir and ssl files is root.

```yaml
ssl_cert:
  dir: "/etc/ssl/selfsigned"
  key:
    filename: "selfsigned.key"
    content: |
      -----BEGIN PRIVATE KEY-----
      ...
      -----END PRIVATE KEY-----
  crt:
    filename: "selfsigned.crt"
    content: |
      -----BEGIN CERTIFICATE-----
      ...
      -----END CERTIFICATE-----
```
Configure the dir for the ssl files, the key filename and content and the crt filename and content. Currently only supports one certificate as I only use one ssl certificate.
