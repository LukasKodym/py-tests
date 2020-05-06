# -*- coding: utf-8 -*-

# %%
##
import rocket.data

# %%
##
dir(rocket.data)

# %%
##
dane = rocket.data.get_data()

# %%
##
import rocket.algorytmy

# %%
##
dir(rocket.algorytmy)

rocket.algorytmy.drezewa_decyzyjne()

# %%
##
from rocket.algorytmy import drezewa_decyzyjne

# %%
##
drezewa_decyzyjne()

# %%
##
from rocket.funkcje.stats import mean

# %%
##
mean(dane)
