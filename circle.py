import math
import unittest

def area(r):
    '''
        Возвращает площадь круга по заданным сторонам.

            Параметры:
                r (int): радиус круга

            Возвращаемые значения:
                area (int): площадь круга
        '''
    return math.pi * r * r


def perimeter(r):
    '''
        Возвращает периметр круга по заданным сторонам.

            Параметры:
                r (int): радиус круга

            Возвращаемые значения:
                perimetr (int): периметр круга
        '''
    return 2 * math.pi * r

class CircleTestCase (unittest.TestCase):
    def test_zero_mul_area(self):
        res = area (0)
        self.assertEqual(res, 0)

    def test_square_mul_area(self):
        res = area(10)
        self.assertEqual(res, 100 * math.pi)

    def test_zero_mul_perimeter(self):
        res = perimeter (0)
        self.assertEqual(res, 0)

    def test_square_mul_perimeter(self):
        res = perimeter(10)
        self.assertEqual(res, 20 * math.pi)


