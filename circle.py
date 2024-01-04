import math
import unittest


def area(r):
    '''
    Принимает число r, возвращает площадь круга с радиусом r.
    Пример вызова функции: area(10.0) -> 314.1592653589793.
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Принимает число r, возвращает длину окуржности с радиусом r.
    Пример вызова функции: perimeter(11) -> 69.11503837897544.
    '''
    return 2 * math.pi * r


class CircleleTestCase(unittest.TestCase):
    def test_area_multiply_by_zer0(self):
        res = area(0)
        self.assertEqual(res, 0)


    def test_positive_area(self):
        res = area(79)
        self.assertAlmostEqual(res, 19606.6798, 4)


    def test_negative_area(self):
        self.assertRaises(ValueError, area, -7865)


    def test_float_area(self):
        res = area(8.2)
        self.assertAlmostEqual(res, 211.2407, 4)


    def test_perimeter_multiply_by_zer0(self):
        res = perimeter(0)
        self.assertEqual(res, 0)


    def test_positive_perimeter(self):
        res = perimeter(18)
        self.assertAlmostEqual(res, 113.0973, 4)


    def test_negative_perimeter(self):
        self.assertRaises(ValueError, perimeter, -76)


    def test_float_perimeter(self):
        res = perimeter(9.2)
        self.assertAlmostEqual(res, 57.8053, 4)
