#!/usr/bin/python3
""" Rectangle module """


class Rectangle:

    number_of_instances = 0

    """ represents a rectangle """
    def __init__(self, width=0, height=0):
        """ Initialize rectangle with optional width & height
            Args:
                width (int, optional): rectangle width, defaults to 0
                height (int, optional): rectangle height, defaults to 0
        """
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """ property to retrieve private instance
            height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ property to set private instance
            height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """ property to retrieve private instance
            width
        """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """ return area of rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ return rectangle perimeter """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

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
        class_name = type(self).__name__
        return "{}({}, {})".format(class_name, self.__width, self.__height)

    def __del__(self):
        """ print text on deletion of an instance of the class
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")