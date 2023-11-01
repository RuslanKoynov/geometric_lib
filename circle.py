import math
import unittest
class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
       res = area(0)
       self.assertEqual(res, 0.0)
       
    def test_area(self):
       res = area(10)
       self.assertEqual(res, 314.1592653589793)

    def test_perimeter(self):
       res = perimeter(7)
       self.assertEqual(res, 43.982297150257104)

def area(r):
    ''' Принимает радиус r, возвращает площадь круга с радиусом r '''
    return math.pi * r * r


def perimeter(r):
    ''' Принимает радиус r, возвращает длину окружности с радиусом r '''
    return 2 * math.pi * r

