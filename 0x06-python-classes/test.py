#!/usr/bin/python

"""Declare square"""

class Square:
    """Represent a square"""
    def __init__(self, size=0, position=(0, 0)):
        """initialize square
            Args:
                size: square size
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get square size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set square size"""
        if not isinstance(value, int):
            raise TypeError("size must be integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        self.__size = value

    @property
    def position(self, value):
        """set square position"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Area of square

            Return:
                    area of square
        """
        return self._Square__size ** 2

    def my_print(self):
        """prints squares with # characters"""
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print()
