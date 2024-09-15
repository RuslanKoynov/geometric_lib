import unittest
from square import area, perimeter
class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)
    def test_area_random_num(self):
        res = area(2)
        self.assertEqual(res, 4)
    def test_area_random_float_num(self):
        res = area(2.4)
        self.assertEqual(res, 5.76)
    def test_area_big_random_num(self):
        res = area(30000000)
        self.assertEqual(res, 900000000000000)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    def test_perimeter_random_num(self):
        res = perimeter(3)
        self.assertEqual(res, 12)
    def test_perimeter_random_float_num(self):
        res = perimeter(2.41)
        self.assertEqual(res, 9.64)
    def test_perimeter_big_random_num(self):
        res = perimeter(30000000)
        self.assertEqual(res, 120000000)
    def test_sum_area_perimeter_random_num(self):
        res = area(5) + perimeter(5)
        self.assertEqual(res, 45)
