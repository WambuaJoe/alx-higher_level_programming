#!/usr/bin/python3
""" Square module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ square class that inherits from rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """ initialize square attributes """
        super().__init__(size, size, x, y)

    def __str__(self):
        """ implement str representation """
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__, self.id,
                                             self.__x, self.__y,
                                             self.__width)
