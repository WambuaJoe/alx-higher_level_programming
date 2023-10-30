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

    def update(self, *args, **kwargs):
        """ assign arguments to attributes """
        if args and len(args) != 0:
            for index, val in enumerate(args):
                if index == 0:
                    self.id = val
                if index == 1:
                    self.size = val
                if index == 2:
                    self.x = val
                if index == 3:
                    self.y = val
        else:
            for key, val in kwargs.items():
                if key == 'id':
                    self.id = val
                if key == 'size':
                    self.size = val
                if key == 'x':
                    self.x = val
                if key == 'y':
                    self.y = val

    def to_dictionary(self):
        """ returns the dictionary representation of a Square """
        return {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}
