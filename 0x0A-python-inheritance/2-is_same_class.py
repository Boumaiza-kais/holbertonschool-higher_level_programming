#!/usr/bin/python3

'''
this module have a function (is_same_class) 
'''


def is_same_class(obj, a_class):
    '''
    a function returns True if the object is exactly an
    instance of the specified class ; otherwise False.
    '''
    return (type(obj) == a_class)
