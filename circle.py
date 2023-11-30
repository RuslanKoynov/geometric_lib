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
    if (r < 0):
        raise ValueError("Negative number")
    else:
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
    def test_area_positive_radius(self):
        res = area(5)
        self.assertAlmostEqual(res, 78.54, places=2)

    def test_area_negative_radius(self):
        with self.assertRaises(ValueError):
            area(-3)

    def test_perimeter_zero_radius(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    
    def test_perimeter_mixed_radius(self):
        res = perimeter(4)
        self.assertAlmostEqual(res, 25.13, places=2)

    def test_area_float_radius(self):
        res = area(2.5)
        self.assertAlmostEqual(res, 19.63, places=2)

    def test_perimeter_float_radius(self):
        res = perimeter(3.5)
        self.assertAlmostEqual(res, 21.99, places=2)
