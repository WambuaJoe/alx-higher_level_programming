#!/usr/bin/python3
""" Rectangle module """


class Rectangle:

    number_of_instances = 0
    print_symbol = '#'

    """ create a rectangle class """
    def __init__(self, width=0, height=0):
        """implement rectangle properties
            Args:
                width (integer, optional): rectangle width, default set to 0
                height (integer, optional): rectangle height default set to 0
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ get value of width """
        return self.__width

    @width.setter
    def width(self, value):
        """ set value of width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ get value of height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set value of height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """ get area of rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ get perimeter of rectangle """
        return (self.__width + self.__height) * 2

    def __str__(self):
        """ string representation for the rectangle class """
        if self.__height == 0 or self.__width == 0:
            return ""
        rectangle_area = ''
        for a in range(self.__height):
            rectangle_area += "#" * self.__width
            if a != self.__height - 1:
                rectangle_area += "\n"
        return rectangle_area

    def __repr__(self):
        """ return string representation that can recreate the
            rectangle object
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ print text on deletion of an instance of the class
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
