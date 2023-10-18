#!/usr/bin/python3
""" Rectangle module """
from models.base import Base


class Rectangle(Base):
    """ class Rectangle that inherits from Base class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialize width, height, x, y """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
