# server.playbooks.pihole
Install and configure pihole on the remote hosts.

## Requirements
None

## Role variables
| Variable                  | Default       | Comments                                                                                                                                           |
|---------------------------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| pihole_custom_dns_entries | []            | Example: <pre>pihole_custom_dns_entries:<br>- ip: 10.1.1.100<br>  url: pihole.custom.dns<br>- ip: 10.1.1.83<br>  url: pihole_test.custom.dns</pre> | 
| pihole_automatic_update   | yes           | Yes will automatically install a new release if one is available. No will prevent this.                                                            | 


