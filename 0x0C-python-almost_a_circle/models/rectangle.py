#!/bin/python3
""" Rectangle module """
from models.base import Base


class Rectangle(Base):
    """ create Rectangle class, that inherits from Base class """
    def __init__(self, width, height, x=0, y=0):
        """ initialize rectangle width, height, x, y """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ return rectangle width """
        return self.__width

    @width.setter
    def width(self, value):
        """ set rectangle width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ return rectangle height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set rectangle height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ return x """
        pass