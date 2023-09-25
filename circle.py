import math


def area(r):
    """Returns an area of the circle

    Args:
        r (integer/double): radius of the circle

    Returns:
        (integer/double): area of the circle
    """
    return math.pi * r * r


def perimeter(r):
    """ Returns a length of the circle

    Args:
        r (integer/double): radius of the circle

    Returns:
        (integer/double): length of the circle
    """
    return 2 * math.pi * r
