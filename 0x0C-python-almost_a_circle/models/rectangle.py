#!/bin/python3
""" Rectangle module """
from models.base import Base


class Rectangle(Base):
    """ create Rectangle class, that inherits from Base class """
    def __init__(self, width, height, x=0, y=0):
        """ initialize rectangle width, height, x, y """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
        return self.__x

    @x.setter
    def x(self, value):
        """ set value of x"""
        if not type(value) == int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ return x """
        return self.__y

    @y.setter
    def y(self, value):
        """ set value of y"""
        if not type(value) == int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
