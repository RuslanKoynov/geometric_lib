import unittest
from circle import area, perimeter
import math
class CircleTestCase(unittest.TestCase):
    def test_circle_area_float(self):
        res = area(8.22)
        self.assertAlmostEqual(res, 212.27, places=2)

    def test_circle_area_negative(self):
        with self.assertRaises(Exception):
            area(-1)
    def test_circle_area_integer(self):
        res = area(10)
        self.assertAlmostEqual(res, 314.16, places=2)

    def test_circle_area_zero(self):
        res = area(0)
        self.assertAlmostEqual(res, 0)

    def test_circle_perimetr_integer(self):
        res = perimeter(6)
        self.assertAlmostEqual(res, 37.7, places=1)

    def test_circle_perimetr_negative(self):
        with self.assertRaises(Exception):
            perimeter(-1)
    def test_circle_perimetr_float(self):
        res = perimeter(2.88)
        self.assertAlmostEqual(res, 18.1, places=1)

    def test_circle_perimeter_zero(self):
        res = perimeter(0)
        self.assertAlmostEqual(res, 0)


