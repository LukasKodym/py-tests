options ={
    'env': 'production',
    'db': "mysql",
    'version': 1.0,
    'show_errors': True
}
options['user'] = "admin"
print(options)
options['version'] = 2.0
print(options['db'])
print(options['version'])