# -*- coding: utf-8 -*-


class Czlowiek:
    pochodzenie = 'Ziemia'
    # imie = 'Jack'


class Polak:
    kraj = 'Polska'
    imie = 'Piotr'


class Pilkarz(Czlowiek, Polak):  # ważna jest kolejnosc klas po których sie dziedziczy

    def info(self):
        print(f'Utworzony obiekt pochodzi z planety {self.pochodzenie}.\n'
              f'Kraj pochodzenia: {self.kraj}\n'
              f'Nazwa obiektu: {self.imie}')


# %%
##
pilkarz_1 = Pilkarz()
pilkarz_1.info()
