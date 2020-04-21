# %%
counter = 0
while counter < 10:
    counter += 1
    if counter == 5:
        break
    print(counter)

# %%
counter = 1
while counter <= 10:
    counter += 1
    if counter % 2 != 0:
        continue
    print(counter)

# %%
while True:
    num = int(input('Podaj liczbę większą od 0: '))
    if num > 0:
        print('Twoja liczba to:', num)
        break
    else:
        print('Twoja liczba nie jest prawidłowa')
