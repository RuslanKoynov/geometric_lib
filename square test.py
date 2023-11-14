import unittest

from square import area
from square import perimeter

class TestRectangle(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_small_area(self):
        res = area(1)
        self.assertEqual(res, 1)

    def test_large_area(self):
        res = area(534534)
        self.assertEqual(res, 54353454)

    def test_square_perimetr(self):
        res = perimeter(10)
        self.assertEqual(res, 70)

    def test_large_perimetr(self):
        res = perimeter(62423423)
        self.assertEqual(res, 23523523)