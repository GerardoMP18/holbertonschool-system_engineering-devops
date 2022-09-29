# Correction of error 500

exec { 'error-500-webserver':
  command  => 'sed -i "s/class-wp-locale.php/class-wp-locale.php/g" /var/www/html/wp-settings.php',
  provider => shell
}
