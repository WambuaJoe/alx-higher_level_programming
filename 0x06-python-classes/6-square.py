#!/usr/bin/python3
""" Square class to represent a class """


class Square:
    """
    defines a Square & its basic properties
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if len(value) == 2 and isinstance(value, tuple) \
            and isinstance(value[0], int) and \
            isinstance(value[1], int) and \
                value[0] > 0 and value[1] > 0:
            self.__position = value
        else:
            raise TypeError("position must be  tuple of 2 positive integers")

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for a in range(self.position[1]):
                print("")
            for a in range(self.size):
                print(" " * self.position[0], end='')
                print("#" * self.size)
