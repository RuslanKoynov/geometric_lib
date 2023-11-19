import math
def area(r):
    if not isinstance(r, (int, float)) or r <= 0:
        return -1
    return math.pi * r * r

'''принимает только положительное число r - радиус окружности, возвращает площадь окружности'''

def perimeter(r):
    if not isinstance(r, (int, float)) or r <= 0:
        return -1
    return 2 * math.pi * r

'''принимает только положительное число r - радиус окружности, возвращает периметр окружности'''
