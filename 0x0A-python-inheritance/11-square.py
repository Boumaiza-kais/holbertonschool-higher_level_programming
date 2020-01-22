#!/usr/bin/python3
'''
this module have a Square class
'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    Square class
    '''
    def __init__(self, size):
        '''
        initializing a class
        '''
        super().integer_validator(size, size)
        super().__init__(size, size)
        self.size = size

    def area(self):
        return self.size ** 2

    def __str__(self):
        return "[Square] {}/{}".format(self.size, self.size)
