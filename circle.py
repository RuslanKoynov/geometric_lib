import math


def area(r):
    '''
    Возвращает площадь круга с радиусом r.

        Параметры:
             r(int): радиус круга

        Возвращаемое значение:
            math.pi * r * r(int): число, равное площади круга

    Пример вызова функции: area(10) -> 314.1592653589793
    '''
    if isinstance(r, bool):
        return 'Invalid input'
    if isinstance(r, str):
        return 'Invalid input'
    if r < 0:
        return 'Invalid input'
    if r == 0:
        return "The figure doesn't exist"
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает длину окружности с радиусом r

    Параметры:
        r(int): десятичное число - радиус окружности

    Возвращаемое значение:
        2 * math.pi * r(float): десятичное число с плавающей точкой, равное длине окружности

    Пример вызова функции: perimeter(10) -> 62.83185307179586
    '''
    if isinstance(r, bool):
        return 'Invalid input'
    if isinstance(r, str):
        return 'Invalid input'
    if r < 0:
        return 'Invalid input'
    if r == 0:
        return "The figure doesn't exist"
    return 2 * math.pi * r


