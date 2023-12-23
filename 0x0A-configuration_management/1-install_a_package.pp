# Using Puppet, install flask from pip3
exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
}

package { 'python3':
  ensure => 'installed',
}

exec { 'install_werkzeug':
  command => '/usr/bin/pip3 install Werkzeug==2.1.1',
}
