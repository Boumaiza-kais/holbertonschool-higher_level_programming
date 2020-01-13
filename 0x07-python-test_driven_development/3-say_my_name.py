#!/usr/bin/python3

'''
Module say_my_name(first_name, last_name="")
have a funtcion that
print firstname and lastname
'''


def say_my_name(first_name, last_name=""):

    '''
    prints first name and lastname
    '''
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
