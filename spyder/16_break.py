# -*- coding: utf-8 -*-

for i in '0123456789':
    i = int(i)
    print(i)
    if i == 6:
        break

print('koniec')

# %%
sample = 'Python Course'
for char in sample:
    if char == ' ':
        break
    print(char)

# %%
for char in 'jan.kowalski@gmail.com':
    if char == '@':
        print('adres email zwerfikowany')
        break

else:
    print('adres email nie jest poprawny')

print('koniec')

# %% walidator
psw = 'jnhvsoics!vd'
if len(psw) >= 10:
    for i in psw:
        if '!' in psw:
            print('Hasło poprawne')
            break
    else:
        print('Hasło niepoprawne')
else:
    print('Hasło niepoprawne')
