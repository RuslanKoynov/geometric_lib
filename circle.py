import math

def area(r):
    """
    Принимает число r(радиус окружности), возвращает площадь окружности
    """
    if (not(isinstance(r, int))):
        raise TypeError("Invalid data type")
    if (r < 0):
        raise ValueError("Invalid value")
    return math.pi * r * r


def perimeter(r):
    """
    Принимает число r(радиус окружности), возвращает периметр окружности
    """
    if (not(isinstance(r, int))):
        raise TypeError("Invalid data type")
    if (r < 0):
        raise ValueError("Invalid value")
    return 2 * math.pi * r
