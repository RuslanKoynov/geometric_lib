import math
'''
Импорт модуля math для использования константы pi
'''

def area(r):
    """
    Функция принимает один параметр: r - радиус круга.
    Возвращает значение площади круга, вычисленной как math.pi * r * r.
    """
    # if r < 0:
    #     raise TypeError

    return math.pi * r * r


def perimeter(r):
    """
    Функция принимает один параметр: r - радиус круга.
    Возвращает значение периметра круга, вычисленное как 2 * math.pi * r.
    """
    # if r < 0:
    #     raise TypeError
    
    return 2 * math.pi * r

