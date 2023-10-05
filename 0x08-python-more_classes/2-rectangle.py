#!/usr/bin/python3
""" Rectangle module """


class Rectangle:
    """ represents a rectangle """
    def __init__(self, width=0, height=0):
        """ Initialize rectangle with optional width & height
            Args:
                width (int, optional): rectangle width, defaults to 0
                height (int, optional): rectangle height, defaults to 0
        """
        self.width = width
        self.height = height

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

    def area(self):
        """ return area of rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ return rectangle perimeter """
        if self.__height == 0 or self.__width == 0:
            print()
        else:
            return 2 * (self.__height + self.__width)
