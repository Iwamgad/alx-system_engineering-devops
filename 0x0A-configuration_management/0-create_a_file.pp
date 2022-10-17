# A puppet program that creates a file in /tmp
# with some specific requirements

file { 'school':
    path    => '/tmp/school',
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet',
}