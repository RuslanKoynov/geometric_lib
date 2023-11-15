import math


def area(r):
    '''Принимает знаечние радиуса r, возвращает площадь квадрат числа r, умноженный на число pi'''
    return math.pi * r * r


def perimeter(r):
    '''Принимает знаечние радиуса r, возвращает произведение числа r, числа pi и числа 2'''
    return 2 * math.pi * r

radis = False
circ_area = area(radis)
print(circ_area)