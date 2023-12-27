import math


def area(r):
    '''
    Вычисляет площадь круга.

    Параметры:
        r (float) - радиус круга
    Возвращаемое значение:
        area (float) - площадь круга
    '''
    if isinstance(r, bool) or isinstance(r, bool) or (not isinstance(r, float) and not isinstance(r, int)) or r < 0:
        raise Exception

    return math.pi * r * r


def perimeter(r):
    '''
    Вычисляет длину окружности.

    Параметры:
        r (float) - радиус круга
    Возвращаемое значение:
        area (float) - длина окружности
    '''

    if isinstance(r, bool) or (not isinstance(r, float) and not isinstance(r, int)) or r < 0:
        raise Exception
    
    return 2 * math.pi * r

