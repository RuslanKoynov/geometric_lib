def area(a, h):
    """
    Return the triangle area.

        arguments:
            a (auto): side of a triangle.
            h (auto): height drawn to a given side of a triangle.

        return value:
             a * h / 2 (auto): product of the height and the side to which
            the height is drawn divided by 2.

    """
    if (type(a) is int or type(a) is float) and (type(h) is int or type(h) is float):
        if a <= 0 or h <= 0:
            return "Input data ERROR: sides cannot be negative or zero"
        else:
            return round(a * h / 2, 4)
    else:
        return "Input data ERROR: sides must be a number"


def perimeter(a, b, c):
    """
    Return the triangle perimeter.

        arguments:
            a (auto): first triangle side.
            b (auto): second triangle side.
            c (auto): third triangle side.

        return value:
            a + b + c (auto): sum of three sides.
    """
    if (type(a) is int or type(a) is float) and (type(b) is int or type(b) is float) and (type(c) is int or type(c) is float):
        if a <= 0 or b <= 0 or c <= 0:
            return "Input data ERROR: sides cannot be negative or zero"
        else:
            if (a + b > c) and (a + c > b) and (c + b > a):
                return a + b + c
            else:
                return "ERROR: this is not a triangle"
    else:
        return "Input data ERROR: sides must be a number"
