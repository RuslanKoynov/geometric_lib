import math


def area(r):
    '''
    Возвращает площадь круга.
    Параметры:
        r (int): десятичное число
    Возвращаемое значение:
        math.pi * r * r (int): площадь круга
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает периметр.
    Параметры:
        r (int): десятичное число
    Возвращаемое значение:
        2 * math.pi * r (int): периметр
    '''
    return 2 * math.pi * r

