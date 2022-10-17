# A puppet program that creates a manifest that kills a process named killmenow

exec { 'pkill killmenow':
    path     => '/usr/bin:/usr/sbin:/bin',
    provider => shell,
}
