# This manifest kills a process
exec {'killmenow':
command => 'pkill -n killmenow',
path    => '/usr/bin/',
}
