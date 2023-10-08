import math


def area(r):
    '''
    Возвращает площадь круга.

        Параметры:
            r(int): радиус круга
        
        Возвращенное значение:
            math.pi * r * r (int): площадь круга 
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает периметр круга.

        Параметры:
            r(int): радиус круга
        
        Возвращенное значение:
            2 * math.pi * r (int): периметр круга 
    '''
    return 2 * math.pi * r

