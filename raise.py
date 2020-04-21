def divide(a, b):
    if b == 0:
        raise ZeroDivisionError('Błąd ogólny')
    return a / b


print('Podaj liczbę a:')
a = int(input())
print('Podaj liczbę b:')
b = int(input())

try:
    r = divide(a, b)
    print('Wynik dzielenia to:')
    print(r)
except ZeroDivisionError:
    print('Nie można podzielić przez 0!')
