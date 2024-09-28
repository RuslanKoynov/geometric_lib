def area(a):
    """
    Return the square area.

        arguments:
            a (auto): side of a square.

        return value:
            a * a (auto): product of 2 side of the square.
    """
    if type(a) is int or type(a) is float:
        if a <= 0:
            return "Input data ERROR: sides cannot be negative or zero"
        else:
            return round(a * a, 4)
    else:
        return "Input data ERROR: sides must be a number"


def perimeter(a):
    """
    Return the square perimeter.

        arguments:
            a (auto): side of a square.

        return value:
             4 * a (auto): quadruple the side of a square.

    """
    if type(a) is int or type(a) is float:
        if a <= 0:
            return "Input data ERROR: sides cannot be negative or zero"
        else:
            return round(4 * a, 4)
    else:
        return "Input data ERROR: sides must be a number"

