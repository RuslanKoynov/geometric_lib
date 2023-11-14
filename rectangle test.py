import unittest

from rectangle import area
from rectangle import perimeter

class TestRectangle(unittest.TestCase):
    def test_zero_mul(self):
        res = area(5, 5)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(11, 10)
        self.assertEqual(res, 120)

    def test_small_area(self):
        res = area(2, 2)
        self.assertEqual(res, 5)

    def test_large_area(self):
        res = area(53462444, 53453636)
        self.assertEqual(res, 5345345554334)

    def test_square_perimetr(self):
        res = perimeter(20, 20)
        self.assertEqual(res, 80)

    def test_large_perimetr(self):
        res = perimeter(53513551, 5345632)
        self.assertEqual(res, 35156444432345)