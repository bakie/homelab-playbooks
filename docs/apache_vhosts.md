# server.playbooks.apache
Configure apache vhosts on the remote hosts.

## Requirements
ssl_cert variable if enable_ssl is being set to true in the apache vhosts config. It will use ssl_cert.dir, ssl_cert.crt.filename and ssl_cert.key.filename. I only use one ssl cert so it is configured this way to not make things complex. Check the [molecule converge](../molecule/apache_vhosts/converge.yml) file for a example.

## Role variables
| Variable             | Default | Comments                                                                       |
|----------------------|---------|--------------------------------------------------------------------------------|
| apache_vhosts_config | []      | A list of apache vhost configs that need to be configured on the remote host. Example: <pre>- name: "proxyPassApp"<br>  server_name: "proxyapp.url.dev"<br>  listen_port: "9090"<br>  enable_ssl: true<br>  template: "proxy_pass"<br>- name: "documentRootApp"<br>  server_name: "docapp.url.dev"<br>  document_root: "/var/www/html"<br>  enable_ssl: true<br>  template: "document_root"</pre> <br>|

Note: The proxy_pass template in the apache_vhosts_config support custom rewrite conditions. These can be added via rewrite_conditions.
```
rewrite_conditions:
  - "RewriteCond %{HTTP:Connection} upgrade [NC]"
  - "RewriteCond %{HTTP:Upgrade} websocket [NC]"

```
