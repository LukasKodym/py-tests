#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 22:18:29 2020

@author: lukas
"""


def fib(num: int):
    a, b = 0, 1
    for i in range(num):
        a, b = b, a + b
    return a


n = int(input('Który wyraz ciągu Fibonacciego policzyć?'
              '\nPodaj numer wyrazu: '))

val = fib(n)

print('{}. wyraz ciągu wynosi: {}'.format(n, val))
