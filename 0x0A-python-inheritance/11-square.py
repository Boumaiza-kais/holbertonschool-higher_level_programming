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
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        return "[Square] {}/{}".format(self.size, self.size)
