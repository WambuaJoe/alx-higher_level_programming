#!/usr/bin/python3
""" Square module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ square class that inherits from rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes a square with size attributes """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Returns a string representation of the Square class """
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__, self.id,
                                             self.x, self.y, self.width)

    @property
    def size(self):
        """ return square size """
        return self.width

    @size.setter
    def size(self, value):
        """ get size of square """
        self.width = value
        self.height = value
