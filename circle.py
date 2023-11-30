import unittest
import math

def area(r):
    '''
    Возвращает площадь круга

        Параметры:
            r (int): радиус круга
        Возвращаемое значение:
            радиус в квадрате, умноженный на число pi
    
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает длину круга

        Параметры:
            r (int): радиус круга
        Возвращаемое значение:
            радиус, умноженный на число pi и на 2ci

    '''
    return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_positive_area(self):
        res = area(10)
        self.assertEqual(res, 314.1592653589793)

    def test_float_area(self):
        res = area(15.5)
        self.assertEqual(res, 750.7964473723101)

    def test_negative_area(self):
        self.assertRaises(ValueError, area, -10)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_positive_perimeter(self):
        res = perimeter(10)
        self.assertEqual(res, 62.83185307179586)

    def test_float_perimeter(self):
        res = perimeter(15.5)
        self.assertEqual(res, 97.34225151783307)

    def test_negative_perimeter(self):
        self.assertRaises(ValueError, perimeter, -10)

        
