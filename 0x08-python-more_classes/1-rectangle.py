#!/usr/bin/python3
""" Rectangle module """


class Rectangle:
    """ define a rectangle with the height
    and width attributes
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def height(self):
        """ property to retrieve private instance
            height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ property to set private instance
            height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """ property to retrieve private instance
            width
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
