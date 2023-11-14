import math

'''Модуль math – один из наиважнейших в Python. Этот модуль предоставляет обширный функционал для работы с числами.'''


def area(r):
   
    '''Принимает  число r - радиус круга.
    Возвращает r в квадрате умноженное на число Pi, т.е. площадь круга.'''

    return math.pi * r * r


def perimeter(r):

     '''Принимает число r - радиус круга.
    Возращает удвоенное произведение числа r на pi, т.е. пириметр круга.'''
    
     return 2 * math.pi * r