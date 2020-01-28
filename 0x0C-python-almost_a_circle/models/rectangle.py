#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    """ Base class of Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
       
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            
            if type(value) != int:
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            
            if type(value) != int:
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

        @property
        def x(self):
            return self.__x

        @x.setter
        def x(self, value):
            
            if type(value) != int:
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x

        @property
        def y(self):
            return self.__y

        @y.setter
        def y(self, value):
            
            if type(value) != int:
                raise TypeError("y must be an integer")
            if value < 0:
                raise ValueError("y msut be >= 0")
            self.__y = value

        def area(self):
            
            return self.__width * self.__height

        def display(self):
        
            for i in range(self.__y):
                print()
        f   for i in range(self.__height):
                for x in range(self.__x):
                    print(" ", end="")
                for j in range(self.__width):
                    print('#', end="")
                print()
            
        def __str__(self):
            return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y, self.width, self.height)
        
