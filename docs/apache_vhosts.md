# server.playbooks.apache
Configure apache vhosts on the remote hosts.

## Requirements
The `ssl_cert` variable is required if `enable_ssl` is being set to true in the apache vhosts config. It will use `ssl_cert.dir`, `ssl_cert.crt.filename` and `ssl_cert.key.filename`. I only use one ssl cert so it is configured this way to not make things complex. Check the [molecule converge](../molecule/apache_vhosts/converge.yml) file for a example.

## Role defaults
Available defaults are listed below, along with default value (see [defaults/main.yml](../roles/apache_vhosts/defaults/main.yml))
```yaml
apache_vhosts_config: []
# apache_vhosts_config:
#   - name: {The name of the vhost config file}
#     server_name: {The server name}
#     listen_port: {port the service is listening on}
#     template: {proxy_pass or document_root}
#     enable_ssl: {if set to true, you must also have set the ssl_cert variable as described n the requirements}
#     document_root: {The document root path. Only required if template is document_root}
#     rewrite_conditions: {a list of rewrite conditions to configure. Only required if template is proxy_pass}
```
A list of apache vhost configs that need to be configured on the remote host. Two types of templating is support, proxy_pass and document_root.
The proxy_pass template supports custom rewrite conditions. These can be added via the rewrite_conditions option.
