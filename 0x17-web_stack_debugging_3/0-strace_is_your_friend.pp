# This script fixes a line for the wordpress server that is not working properly
exec { 'fixing a line':
        command => 'sudo sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php'
    }
