# -*- coding: utf-8 -*-
# %%
##

class Drzewo:

    def wyswietl_info_o_drzewie(self):
        # pass
        self.nazwa = 'Sosna'
        self.wiek = 30
        print(f'Drzewo {self.nazwa} ma {self.wiek}.')


drzewo = Drzewo()

# %%
##
drzewo.wyswietl_info_o_drzewie()

# %%
##
Drzewo.wyswietl_info_o_drzewie(drzewo)
