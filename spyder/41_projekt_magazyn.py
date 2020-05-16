# -*- coding: utf-8 -*-

# import sys
# sys.exit() 


class Magazyn:

    def __init__(self, lista_produktow):
        self.lista_produktow = lista_produktow

    def wydruk_listy(self):
        for produkt in self.lista_produktow:
            print(produkt)

    def wyswietl_dostepne_produkty(self):
        if self.lista_produktow == []:
            print('\nMagazyn jest pusty.\n\n***********************')
        else:
            print('Dostepne produkty:\n')
            self.wydruk_listy()

    def dodaj_produkt(self):
        self.nazwa_produktu = input('Podaj nazwę produktu: >>> ')
        if self.nazwa_produktu not in self.lista_produktow:
            self.lista_produktow.append(self.nazwa_produktu)
        print(f'\nProdukt {self.nazwa_produktu} został dodany do magazynu.\n')
        self.wydruk_listy()

    def usun_produkt(self):
        self.nazwa_produktu = input('Podaj nazwę produktu, który chcesz '
                                    'usunąć: >>> ')
        if self.nazwa_produktu in self.lista_produktow:
            self.lista_produktow.remove(self.nazwa_produktu)
            print('\nUsunięto produkt z magazynu.\n')
            self.wydruk_listy()
        else:
            print('\nPodanego produktu nie ma na magazynie.')


# %%
##
magazyn = Magazyn([])

while True:
    print('\nWprowadź 1 aby wyswietlić stan magazynu.')
    print('Wprowadź 2 aby dodać produkt.')
    print('Wprowadź 3 aby usunąć produkt.')
    print('Wprowadź 4 aby zakończyć')
    wybor_uzytkownia = input('>>> ')

    if wybor_uzytkownia == str('1'):
        magazyn.wyswietl_dostepne_produkty()
    elif wybor_uzytkownia == str('2'):
        magazyn.dodaj_produkt()
    elif wybor_uzytkownia == str('3'):
        magazyn.usun_produkt()
    elif wybor_uzytkownia == str('4'):
        print('\nKoniec programu...')
        break
    else:
        print('\nBłędny wybór, spróbuj jeszcze raz.')
