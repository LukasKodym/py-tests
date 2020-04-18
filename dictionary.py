# %%
options = {
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

# %%
options = {
    'env': 'production',
    'db': "mysql",
    'version': 1.0,
    'show_errors': True
}
print(options.get('version'))
del options['db']

options.update({
    'user': 'admin',
    'app': 0,
    'version': 2.2
})

print(options)
print(options.get('db'))
print(options.get('version'))

for key in options:
    print(options[key])
print(options.values())
print(options.keys())
