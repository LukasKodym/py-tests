try:
    print('próbujemy podzielić')
    a = 2 / 'aa'
    print(a)
except ZeroDivisionError:
    print('Błąd - dzielnie przez zero')
except TypeError:
    print('Błąd - niewłaściwy typ dzielnika')
