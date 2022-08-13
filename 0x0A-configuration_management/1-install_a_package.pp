# Install flask with puppet
# ensure   => 2.1.0 version to install
# provider => pip3  providor to install

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
