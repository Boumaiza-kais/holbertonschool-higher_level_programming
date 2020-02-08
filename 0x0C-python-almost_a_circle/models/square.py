#!/usr/bin/python3
'''
This module contain the class square
'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    class Square Base
    '''

    def __init__(self, size, x=0, y=0, id=None):
        '''instatiation of the base'''
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        '''size property'''
        return self.width

    @size.setter
    def size(self, value):
        '''size setter'''
        self.width = value
        self.height = value

    def __str__(self):
        '''__str__ func'''
        message = "[Square] ({}) {}/{} - {}"
        return message.format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        '''update fun'''
        if len(args) != 0:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        '''to_dictionary fun'''
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
