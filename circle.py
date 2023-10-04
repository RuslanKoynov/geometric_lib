import math

def area(r):
    """
    Функция, которая вычисляет площадь круга по его радиусу.

    Args:
        r (float): Радиус круга.

    Returns:
        float: Площадь круга.
    """
    return math.pi * r * r

def perimeter(r):
    """
    Функция, которая вычисляет периметр окружности по ее радиусу.

    Args:
        r (float): Радиус окружности.

    Returns:
        float: Периметр окружности.
    """
    return 2 * math.pi * r


