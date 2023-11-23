import math
import unittest

def area(r):
    '''
    Возвращает площадь круга.

        Параметры:
            r(int): радиус круга
        
        Возвращенное значение:
            math.pi * r * r (int): площадь круга 
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает периметр круга.

        Параметры:
            r(int): радиус круга
        
        Возвращенное значение:
            2 * math.pi * r (int): периметр круга 
    '''
    return 2 * math.pi * r


class CircleTestCase(unittest.TestCase):
    def test_area_1(self):
        res = area(5)
        self.assertAlmostEqual(res, 78.53981633974483)
       
    def test_area_2(self):
        res = area(17.5)
        self.assertAlmostEqual(res, 962.1127501618741)

    def test_area_3(self):
        with self.assertRaises(Exception):
            area(-10)

    def test_perimeter_1(self):
        res = perimeter(5)
        self.assertEqual(res, 31.41592653589793)
    
    def test_perimeter_2(self):
        res = perimeter(17.5)
        self.assertAlmostEqual(res, 109.95574287564276)
    
    def test_perimeter_3(self):
        with self.assertRaises(Exception):
            perimeter(-10)