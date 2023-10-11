#!/usr/bin/python3
""" Rectangle Module """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class Rectangle """

    def __init__(self, width, height):
        """ initialize rectangle with width & height
            Args:
                width - rectangle width, integer
                height - rectangle height, integer
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
