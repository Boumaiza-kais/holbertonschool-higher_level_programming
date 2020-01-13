#!/usr/bin/python3
'''
Module have add_integer function
add_integer adds two integers
(a and b)
'''


def add_integer(a, b=98):
    '''
    Returns the additon of two integers (a and b).
    '''
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
