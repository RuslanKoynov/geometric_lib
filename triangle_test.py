import unittest
from triangle import area, perimeter
class TriangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0, 0)
        self.assertEqual(res, 0)
    def test_area_random_num(self):
        res = area(2,3)
        self.assertEqual(res, 3)
    def test_area_random_float_num(self):
        res = area(2.4,3.6)
        self.assertEqual(res, 4.32)
    def test_area_big_random_num(self):
        res = area(20000, 30000000)
        self.assertEqual(res, 300000000000)

    def test_perimeter_zero(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)
    def test_perimeter_random_num(self):
        res = perimeter(3,2, 4)
        self.assertEqual(res, 9)
    def test_perimeter_random_float_num(self):
        res = perimeter(2.41, 3.66, 4.15)
        self.assertEqual(res, 10.22)
    def test_perimeter_big_random_num(self):
        res = perimeter(20000000, 30000000, 2000000000)
        self.assertEqual(res, 2050000000)
    def test_sum_area_perimeter_random_num(self):
        res = area(5, 9) + perimeter(5, 4, 3)
        self.assertEqual(res, 34.5)
