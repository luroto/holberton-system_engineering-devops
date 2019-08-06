# This script adds a new line in the config file for ssh
file { '~/.ssh/config':
ensure => 'present',
}

file_line { 'appendingkey':
path => '~/.ssh/config',
line => 'IdentityFile ~/.ssh/holberton',
}

file_line { 'appendingpasswordoff':
path => '~/.ssh/config',
line => 'PasswordAuthentication no',
}
