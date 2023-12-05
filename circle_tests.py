import unittest
from circle import area, perimeter
import math
class CircleTestCase(unittest.TestCase):
    def test_circle_area_float(self):
        res = area(8.22)
        self.assertAlmostEqual(res, 212.27, places=2)

    def test_circle_area_negative(self):
        res = area(-1)
        self.assertEqual(res, "ERROR")
    def test_circle_area_integer(self):
        res = area(10)
        self.assertAlmostEqual(res, 314.15, places=2)

    def test_circle_area_zero(self):
        res = area(0)
        self.assertAlmostEqual(res, 0)

    def test_circle_perimetr_integer(self):
        res = perimeter(6)
        self.assertAlmostEqual(res, 37.69, places=2)

    def test_circle_perimetr_negative(self):
        res = perimeter(-1)
        self.assertEqual(res, "ERROR")

    def test_circle_perimetr_float(self):
        res = perimeter(2.88)
        self.assertAlmostEqual(res, 18.09, places=2)

    def test_circle_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)


