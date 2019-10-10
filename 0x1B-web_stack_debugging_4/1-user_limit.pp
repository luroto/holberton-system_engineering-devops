# This script changes the ULIMIT of nginx
exec { 'suspending nginx':
    command  => '/bin/sed -i "s/hard nofile 5/hard nofile 10000/g"'\
              'bin/sed -i "s/soft nofile 4/soft nofile 20000/g"',
    provider => shell
    }
