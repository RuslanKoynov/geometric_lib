import math
'''
Импорт модуля math для использования константы pi
'''

def area(r):
    return math.pi * r * r
"""
    Функция принимает один параметр: r - радиус круга.
    Возвращает значение площади круга, вычисленной как math.pi * r * r.
"""

def perimeter(r):
    return 2 * math.pi * r
"""
    Функция принимает один параметр: r - радиус круга.
    Возвращает значение периметра круга, вычисленное как 2 * math.pi * r.
"""