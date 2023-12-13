import unittest

import math
'''
Модуль math предоствляет обширный функционал для проведения вычислений 
с вещественными числами(числами с плавающей точкой).
'''
def area(r):
    '''
    Принимает число, которое  является радиусом круга: r
    Возвращает площадь круга, вычисляя ее по формуле: π * r^2
    '''
    return math.pi * r * r
def perimeter(r):
    '''
    Принимает число, которое  является радиусом круга: r
    Возвращает периметр круга, вычисляя его по формуле: 2 * π * r
    '''
    return 2 * math.pi * r


class CircleTestCase(unittest.TestCase):
    def test_area_1(self):
        res = area(1)
        self.assertEqual(res, math.pi)

    def test_area_0(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_perimetr_1(self):
        res = perimeter(1)
        self.assertEqual(res, 2*math.pi)

    def test_perimetr_0(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

