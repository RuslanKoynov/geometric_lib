import unittest
import math

class CircleTestCase(unittest.TestCase):
    def area_test_zero(self):
        res = area(0)
        self.assertEqual(res, 0.0)

    def area_test_number(self):
        res = area(5)
        self.assertEqual(res, 78.53981633974483)

    def area_test_float_number(self):
        res = area(3.5)
        self.assertEqual(res,38.48451000647496)

    def perimeter_test_zero(self):
        res = perimeter(0)
        self.assertEqual(res,0)

    def perimeter_test_number(self):
        res = perimeter(5)
        self.assertEqual(res,31.41592653589793)

    def perimeter_test_float_number(self):
        res = perimeter(2.2455)
        self.assertEqual(res,14.108892607271759)



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

