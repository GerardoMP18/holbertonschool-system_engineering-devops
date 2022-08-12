# Create a file
# ensure ---> present = create new file if not exits the file
# mode   ---> 0744    = the desired permission mode for the file
# owner  --->         = The user to whom the file should belong
# group  --->         = Which group should own the file
# content -->         = The desired contens of a file
file { '/tmp/school':
  ensure  => '1.1.0',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet'
}
