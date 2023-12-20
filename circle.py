import math
import unittest


def area(r):
    ''' Принимает десятичное число r, возрващает квадрат числа r, умноженный на число Пи'''
    return math.pi * r * r


def perimeter(r):
    ''' Принимает десятичное число r, возвращает число r, умноженное на 2 и на число Пи'''
    return 2 * math.pi * r


print(perimeter(6))
