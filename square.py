def area(a):
    """
    Принимает число a(сторона квадрата), возвращает площадь квадрата
    """
    if (not(isinstance(a, int))):
        raise TypeError("Invalid data type")
    if (a < 0):
        raise ValueError("Invalid value")
    return a * a


def perimeter(a):
    """
    Принимает число a(сторона квадрата), возвращает периметр квадрата
    """
    if (not(isinstance(a, int))):
        raise TypeError("Invalid data type")
    if (a < 0):
        raise ValueError("Invalid value")
    return 4 * a
    