# -*- coding: utf-8 -*-

text = 'Witaj na kursie Pythona.\nPython jest super!'

print(text)

# %%

dir(text)
help(str.count)

# %%
text.capitalize()

# %%
text.title()

# %%
text.count('Python')

# %%
text.startswith('witaj')
'python'.startswith('py')

# %%
text.endswith('r!')

# %%
'sample.py'.endswith('.py')

# %%
text.find('Python')
text[text.find('Python'):]

# %%
hashtags = 'sport#gym'
idx = hashtags.find('#')
hashtags[:idx]

# %%
'pawel5555 '.isalnum()

# $$
'43434ljkjhk'.isdigit()

# %%
'pyThon'.islower()
'PAwEL'.isupper()

# %%
' '.join(['python', '3,7'])
'#'.join(['sport', 'gym', 'fit'])
','.join(['1', '2', '3', '4'])

# %%
'#good#time#mood'.replace('#', ' ')
'column name'.replace(' ', '_')

# %%
'    python       '.strip()
'    python       '.rstrip()
'    python       '.lstrip()

# %%
'1,2,3,4,5'.split(',')
'java python php sql sas'.split()
'#gym#fit#mood'.split('#')

# %%
'12'.zfill(5)
'1'.zfill(10)

# %%
'#'.join(['sport','python','free','time'])

x = '123,785,45,5'
print(x.split(','))
