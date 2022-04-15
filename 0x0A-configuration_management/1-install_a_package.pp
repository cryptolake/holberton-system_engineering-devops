# install package
package { 'puppet-lint':
  ensure   => 'present',
  provider => 'gem',
}
