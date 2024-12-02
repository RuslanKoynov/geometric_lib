from triangle import area, perimeter
import unittest

class TriangleTestCase(unittest.TestCase):

    def test_area_positive(self):
        res = area(11, 22)
        self.assertEqual(res, 121)

    def test_area_negative(self):
            with self.assertRaises(Exception):
                area(-5,-3)

    def test_area_zero(self):
        res = area(0, 0)
        self.assertEqual(res, 0.0)

    def test_area_real(self):
        res = area(54.23, 65.12)
        self.assertEqual(res, 1765.7288)

    def test_perimeter_positive(self):
        res = perimeter(123, 543,44)
        self.assertEqual(res, 710)

    def test_perimeter_negative(self):
            with self.assertRaises(Exception):
                perimeter(-234,-123,-12)

    def test_perimeter_zero(self):
        res = perimeter(0, 0,0)
        self.assertEqual(res, 0.0)

    def test_perimeter_real(self):
        res = perimeter(324.123, 5.23,87.234)
        self.assertEqual(res, 416.587)
