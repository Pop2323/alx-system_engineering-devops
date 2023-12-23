exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
}

exec { 'install_python':
  command => '/usr/bin/pip3 install python==3.8.10',
}

exec { 'install_werkzeug':
  command => '/usr/bin/pip3 install Werkzeug==2.1.1',
}
