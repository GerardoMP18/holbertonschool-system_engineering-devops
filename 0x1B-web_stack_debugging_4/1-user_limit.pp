# Change of user limits

exec { 'configuration-user':
  command  => 'sudo sed -i "s/nofile */nofile 50000/g" /etc/security/limits.conf',
  provider => 'shell'
}
