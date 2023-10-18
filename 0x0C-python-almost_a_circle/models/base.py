#!/usr/bin/python3
""" Base module """


class Base:
    """ create Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ instantiate Base class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
