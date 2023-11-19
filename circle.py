import math
def area(r):
    if r <= 0:
        return -1
    return math.pi * r * r

'''принимает только положительное число r - радиус окружности, возвращает площадь окружности'''
print(area(1))
def perimeter(r):
    if r <= 0:
        return -1
    return 2 * math.pi * r

'''принимает только положительное число r - радиус окружности, возвращает периметр окружности'''
print(perimeter(1))
