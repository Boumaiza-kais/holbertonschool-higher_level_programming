#!/usr/bin/python3

"""
this module have a function (add_attribute)
"""


def add_attribute(objec, attribute, value):
    """
    a function that adds a new attribute to an object
    """
    if hasattr(objec, "__dict__"):
        setattr(objec, attribute, value)
    else:
        raise TypeError("can't add new attribute")
