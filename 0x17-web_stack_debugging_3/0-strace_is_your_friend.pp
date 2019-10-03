exec { 'fixing a line':
        command => 'sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php',
        cwd     => '/var/www/html/wp-settings.php',
        shell   => '/bin/bash'
}
