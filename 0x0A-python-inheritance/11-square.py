#!/usr/bin/python3
""" Square module """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ define subclass Square of parent class Rectangle"""
    def __init__(self, size):
        """ initialize Square length
            Args:
                size: length of any side, integer
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size ** 2

    def __str__(self):
        """ returns description of Square """
        return "[{}] {}/{}".format(type(self).__name__,
                                   self.__size, self.__size)
