import unittest

import math

def area(a, h):
    '''
    Принимает два числа, одно из них является стороной треугольника, другое его высотой: a, h
    Возвращает площадь треугольника, вычисляя ее по формуле: (a * h) / 2
    '''
    return a * h / 2
def perimeter(a, b, c):
    '''
    Принимает три числа, которые являются сторонами треугольника: a, b, c
    Возвращает периметр треугольника, вычисляя его по формуле: a + b + c
    '''
    return a + b + c

class TriangleTestCase(unittest.TestCase):
    def test_area_4_and_2(self):
        res = area(4, 2)
        self.assertEqual(res, 4)

    def test_area_1_and_2(self):
        res = area(1,2)
        self.assertEqual(res, 1)

    def test_perimetr_1_and_1_and_1(self):
        res = perimeter(1,1,1)
        self.assertEqual(res, 3)

    def test_perimetr_1_and_2_and_3(self):
        res = perimeter(1,2,3)
        self.assertEqual(res, 6)