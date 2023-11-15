import unittest
import math
def area(r):
    return math.pi * r * r
    'Принимает число, которое является радиусом круга r'
    'возвращает площадь круга,вычисляя ее по формуле: π*r^2'
def perimeter(r):
    return 2 * math.pi * r
    'Принимает число, которое является радиусом круга r'
    'возвращает площадь круга,вычисляя ее по формуле: π*r'
class CircleTestCase (unittest.TestCase):
    def test_area_zero_r(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_two(self):
        res = area(2)
        self.assertEqual(res, 4*math.pi)

    def test_perimetr_zero(self):
        res = perimeter(0)
        self.assertEqual(res,  0)

    def test_perimetr_two(self):
        res = perimeter(2)
        self.assertEqual(res,  4*math.pi)

if __name__ == '__main__':
    unittest.main()
