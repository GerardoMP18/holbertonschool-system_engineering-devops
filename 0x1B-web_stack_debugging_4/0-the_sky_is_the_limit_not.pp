# This for the change limit  of request in server nginx

exec { 'error-limit-request':
  command  => 'sed -i "s/-n 15/-n 4096/g" /etc/default/nginx && sudo service nginx restart',
  provider => shell
}
