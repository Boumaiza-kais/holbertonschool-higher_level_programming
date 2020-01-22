#!/usr/bin/python3
"""
This modules have MyInt 
"""


class MyInt(int):
    """
    MyInt class
    """
    def __ne__(self, other):
        return (not super().__ne__(other))

    def __eq__(self, other):
        return (not super().__eq__(other))
