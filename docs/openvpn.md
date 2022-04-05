# server.playbooks.openvpn
Install and configure openvpn on the remote hosts.

## Requirements
None

## Role variables
| Variable            | Default                  | Comments                                             |
|---------------------|--------------------------|------------------------------------------------------|
| openvpn_name        | "openvpn_name"           | The name of this specific vpn client connection      |
| openvpn_remote      | "default_openvpn_remote" | The endpoint of the openvpn server                   |
| openvpn_remote_port | 443                      | The port for the openvpn_remote.                     |
| openvpn_ca          | "openvpn_ca"             | The ca needed to connect to the openvpn_remote       |
| openvpn_cert        | "openvpn_cert"           | The cert needed to connect to the openvpn_remote     |
| openvpn_key         | "openvpn_key"            | The key needed to connect to the openvpn_remote      |
| openvpn_tls_auth    | "openvpn_tls_auth"       | The tls_auth needed to connect to the openvpn_remote |
