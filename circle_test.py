import unittest
import math
from circle import perimeter, area
class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)
    def test_area_random_num(self):
        res = area(2)
        self.assertEqual(res, 4 * math.pi)
    def test_area_random_float_num(self):
        res = area(2.4)
        self.assertEqual(res, 5.76 * math.pi)
    def test_area_big_random_num(self):
        res = area(2000)
        self.assertEqual(res, 4000000 * math.pi)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    def test_perimeter_random_num(self):
        res = perimeter(3)
        self.assertEqual(res, 6 * math.pi)
    def test_perimeter_random_float_num(self):
        res = perimeter(2.41)
        self.assertEqual(res, 4.82 * math.pi)
    def test_perimeter_big_random_num(self):
        res = perimeter(20000000)
        self.assertEqual(res, 40000000 * math.pi)
    def test_sum_area_perimeter_random_num(self):
        res = area(5) + perimeter(5)
        self.assertEqual(res, 35 * math.pi)
