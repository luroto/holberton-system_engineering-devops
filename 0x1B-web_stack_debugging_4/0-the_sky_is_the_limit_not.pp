# This script changes the ULIMIT of nginx
exec { 'suspending nginx':
    command  => 'service nginx stop',
    provider => shell
    }

exec { 'changing ULIMIT':
    command  => '/bin/sed -i "s/-n 15/-n 2000/g" /etc/default/nginx',
    provider => shell,
    require  => Exec['suspending nginx']
    }

exec { 'restarting NGINX':
    command  => 'service nginx restart',
    provider => shell,
    require  => Exec['changing ULIMIT']
    }
