import math


def area(r):
    #функция принимает радиус окружности, функция возвращает площадь окружности
    return math.pi * r * r

def perimeter(r):
    #функция принемает радиус окружности, функция возращает периметр окружности
    return 2 * math.pi * r

print(perimeter(10))