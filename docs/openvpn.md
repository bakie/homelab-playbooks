# server.playbooks.openvpn
Install and configure openvpn on the remote hosts.

## Requirements
You need to add a custom ovpn file under the templates dir and change the openvpn_name variable to the name of the file wihout the ovpn.j2 extension.
For example: for the [dummy.ovpn.j2](../roles/openvpn/templates/dummy.ovpn.j2) file the openvpn_name would be `dummy`.

## Role defaults
Available defaults are listed below, along with default value (see [defaults/main.yml](../roles/openvpn/defaults/main.yml))
```yaml
openvpn_auth_user_pass_file_path: "/etc/openvpn/auth_user_pass
```
The file path for the auth-user-pass option in the ovpn file.

```yaml
openvpn_name: "openvpn_name"
```
The type of openvpn template to use. Currently there is only a [dummy.ovpn.j2](../roles/openvpn/templates/dummy.ovpn.j2) file present. You can add your custom ovpn file under templates. This name is also used to name the service (openvpn@openvpn_name).

```yaml
openvpn_username: "openvpn_user"
openvpn_password: "openvpn_password"
```
Credentials for connecting to the VPN.
