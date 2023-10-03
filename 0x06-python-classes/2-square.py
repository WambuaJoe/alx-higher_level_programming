#!/usr/bin/python3
""" Square class to represent a class """


class Square:
    """
    defines a Square & its basic properties
    """
    def __init__(self, size=0):
        try:
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
        except Exception as err:
            print(err)
        else:
            self.__size = size
