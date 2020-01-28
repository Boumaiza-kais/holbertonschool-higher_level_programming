#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)
    def update(self, *args, **kwargs):
        if args != None and len(args):
                for args in args:
                    if args > 0:
                        self.id = arg
                    if args > 1:
                        self.width = arg
                    if args > 2:
                        self.height = arg
                    if args > 3:
                        self.x = arg
                    if args > 4:
                       self.y = arg
        if kwargs != None:
                for key, value in kwargs.items():
                        setattr(self, key, value)

    def to_dictionary(self):
        return {"id": self.id, "width": self.__width, "height": self.__height,
             "x": self.__x, "y":self.__y}
