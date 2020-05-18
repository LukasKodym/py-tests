# -*- coding: utf-8 -*-

def add(x, y):
    """
    Zwraca sumę dwóch liczb
    """
    return x + y
    
if __name__ == '__main__':
    import doctest
    doctest.testfile('test.txt')