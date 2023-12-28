import math


def area(r):
    """
    Возвращает площадь окружности

        Параметры:
            r (float): радиус окружности

        Возвращаемое значение:
            area (float): площадь окружности
    """
    return math.pi * r * r


def perimeter(r):
    """
    Возвращает периметр окружности

        Параметры:
            r (float): радиус окружности

        Возвращаемое значение:
            area (float): периметр окружности
    """
    return 2 * math.pi * r
