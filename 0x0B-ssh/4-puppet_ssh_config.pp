# This script adds a new line in the config file for ssh
exec {'appendingpasswordoff':
command  => '/bin/echo -e "IdentityFile ~/.ssh/holberton\nPasswordAuthentication no" >> /etc/ssh/ssh_config',
provider => 'shell';
}
