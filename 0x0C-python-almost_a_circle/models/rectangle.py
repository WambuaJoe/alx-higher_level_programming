#!/usr/bin/python3
""" Rectangle Module """
from models.base import Base


class Rectangle(Base):
    """ Rectangle Class, inheriting from Class Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes width, height, x, y """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Returns width of rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets rectangle width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Returns rectangle height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets height of rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ Return x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Set x """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ Return y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Set y """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """ return area of rectangle """
        return self.__width * self.__height

    def display(self):
        """ print in stdout """
        for a in range(self.__y):
            print("")
        for a in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """ implement str representation """
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                                                self.__x, self.__y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ assign args to each attribute """
        if args and len(args) != 0:
            for index, value in enumerate(args):
                if index == 0:
                    self.id = value
                if index == 1:
                    self.__width = value
                if index == 2:
                    self.__height = value
                if index == 3:
                    self.__x = value
                if index == 4:
                    self.__y = value
        else:
            for key, val in kwargs.items():
                if key == 'id':
                    self.id = val
                if key == 'width':
                    self.__width = val
                if key == 'height':
                    self.__height = val
                if key == 'x':
                    self.__x = val
                if key == 'y':
                    self.__y = val
