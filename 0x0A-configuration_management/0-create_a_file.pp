# Create a file
# ensure ---> file    = ensures it’s a normal file, and enables use
# mode   ---> 0744    = the desired permission mode for the file
# owner  --->         = The user to whom the file should belong
# group  --->         = Which group should own the file
# content -->         = The desired contens of a file

file { '/tmp/school':
  ensure  => 'file',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet'
}
