import unittest

from square import area
from square import perimeter

class TestSquare(unittest.TestCase):
    def test_area_normal(self):
        res = area(5)
        self.assertEqual(res, 25)

    def test_area_null(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_negative(self):
        res = area(-5)
        self.assertRaises(res, Exception)

    def test_perimetr_normal(self):
        res = perimeter(20)
        self.assertEqual(res, 80)

    def test_perimetr_null(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimter_negative(self):
        res = perimeter(-5)
        self.assertRaises(res, Exception)