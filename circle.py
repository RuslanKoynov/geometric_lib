import math


def area(r):
    """
    Return the circle area.

        arguments:
            r (auto): circle radius.

        return value:
            math.pi * r * r (auto): π multiply by circle radius.
    """
    if type(r) is int or type(r) is float:
        if r <= 0:
            return "Input data ERROR: radius cannot be negative or zero"
        else:
            return round(math.pi * r * r, 4)
    else:
        return "Input data ERROR: radius must be a number"


def perimeter(r):
    """
    Return the circle perimeter.

        arguments:
            r (auto): circle radius.

        return value:
            2 * math.pi * r (auto): 2 multiply by π multiply by circle radius.
    """
    if type(r) is int or type(r) is float:
        if r <= 0:
            return "Input data ERROR: radius cannot be negative or zero"
        else:
            return round(2 * math.pi * r, 4)
    else:
        return "Input data ERROR: radius must be a number"
