#!/usr/bin/python3
def add_integer(a, b=98):
    """ this function calculates the addition of 2
        integers & returns the value of the sum

        Args:
            a(int/float)
            b(int/float)
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    elif isinstance(a, float) or isinstance(b, float):
        a = int(a)
        b = int(b)

    return a + b

print(add_integer(float('inf'), float('-inf')))