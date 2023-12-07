import unittest
import math


def area(r):
    '''
    Возвращает площадь окружности радиусом r.

        Параметры:
            r(int): радиус окружности

        Возвращаемое значение:
             math.pi * r * r(int): площадь окружности
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает периметр окружности радиусом r.

        Параметры:
            r(int): радиус окружности

        Возвращаемое значение:
             2 * math.pi * r(int): периметр окружности
    '''
    return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):
    def test_area_test_zero(self):
        res = area(0)
        self.assertEqual(res, 0.0)

    def test_area_test_number(self):
        res = area(5)
        self.assertAlmostEqual(res, 78.54,places=2)

    def test_area_test_float_number(self):
        res = area(3.5)
        self.assertAlmostEqual(res,38.48,places=2)

    def test_perimeter_test_zero(self):
        res = perimeter(0)
        self.assertAlmostEqual(res,0)

    def test_perimeter_test_number(self):
        res = perimeter(5)
        self.assertAlmostEqual(res,31.42,places=2)

    def test_perimeter_test_float_number(self):
        res = perimeter(2.2455)
        self.assertAlmostEqual(res,14.11,places=2)

    def test_area_test_negative_number(self):
        res = area(-1)
        self.assertEqual(res,"ERROR")

    def test_perimeter_test_negative_number(self):
        res = perimeter(-1)
        self.assertEqual(res,"ERROR")