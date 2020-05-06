# -*- coding: utf-8 -*-

# %%
##
text = 'Python jest wspaniały. Python jest elastyczny. Python rządzi.'

words = text.lower().replace('.', '').split()

unique_words = {word for word in words}
print(unique_words)

# %%
##
unique_words_gt_4 = {word for word in words if len(word) > 4}
print(unique_words_gt_4)

# %%
##
{word.capitalize() if word.startswith('pyt') else word for word in words}

# %%
##
text_2 = 'python jest popularny w uczeniu maszynowym'

unique_words_2 = {word for word in text_2}
print(len(unique_words_2))

# %%
##
text_3 = 'python jest popularny w uczeniu maszynowym'
print(len({word for word in list(text_3)}))
