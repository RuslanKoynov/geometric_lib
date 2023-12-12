import math
'''
Модуль math предоставляет обширный функционал для проведения вычислений
с вещественными числами (числами с плавающей точкой).
'''

def area(r):
    '''
    Принимает число, которое является радиусом круга: r
    Возвращает площадь круга, вычисляя её по формуле: π * r^2
    '''
    if (r < 0):
        raise ValueError("Invalid value")
    return math.pi * r * r


def perimeter(r):
    '''
    Принимает число, которое является радиусом круга: r
    Возвращает периметр круга, вычисляя его по формуле: P = 2 * π * r
    '''
    if (r < 0):
        raise ValueError("Invalid value")
    return 2 * math.pi * r

