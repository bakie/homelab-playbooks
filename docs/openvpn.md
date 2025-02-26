# server.playbooks.openvpn
Install and configure openvpn on the remote hosts.

## Requirements
None

## Role variables
| Variable                         | Default                      | Comments                                                                         |
|----------------------------------|------------------------------|----------------------------------------------------------------------------------|
| openvpn_auth_user_pass_file_path | "/etc/openvpn/auth_user_pass | The file path for the auth-user-pass option in the ovpn file                     | 
| openvpn_name                     | "openvpn_name"               | The name used when creating the ovpn file and the service (openvpn@openvpn_name) |
| openvpn_username                 | "openvpn_user"               |                                                                                  |
| openvpn_password                 | "openvpn_password"           |                                                                                  |
