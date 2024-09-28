def area(a, b):
    """
    Return the rectangle area.

        arguments:
            a (auto): first rectangle parameter.
            b (auto): second rectangle parameter.

        return value:
            a * b (auto): product of width and length of the rectangle.
    """
    if (type(a) is int or type(a) is float) and (type(b) is int or type(b) is float):
        if a <= 0 or b <= 0:
            return "Input data ERROR: sides cannot be negative or zero"
        else:
            return a * b
    else:
        return "Input data ERROR: sides must be a number"


def perimeter(a, b):
    """
    Return the rectangle perimeter.

        arguments:
            a (auto): first rectangle parameter.
            b (auto): second rectangle parameter.

        return value:
            (a + b) * 2 (auto): double the sum of the width and length of
            the rectangle.
    """
    if (type(a) is int or type(a) is float) and (type(b) is int or type(b) is float):
        if a <= 0 or b <= 0:
            return "Input data ERROR: sides cannot be negative or zero"
        else:
            return (a + b) * 2
    else:
        return "Input data ERROR: sides must be a number"

