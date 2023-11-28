import unittest

from circle import area
from circle import perimeter

class TestCircle(unittest.TestCase):
    def test_circle_area_null(self):
        res = area(0)
        self.assertEqual(res, 0)
    def test_circle_area_normal(self):
        res = area(1)
        self.assertEqual(res, 3.141592653589793)
    def test_area_negative(self):
        res = area(-5)
        self.assertRaises(res, 0)

    def test_perimetr_null(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimetr_normal(self):
        res = perimeter(5)
        self.assertEqual(res, 31.41592653589793)

    def test_large_perimetr_negative(self):
        res = perimeter(-15)
        self.assertRaises(res, 0)
