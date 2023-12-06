from triangle import area, perimeter
import unittest

class TriangleTestCase(unittest.TestCase):
    def test_triangle_area_integer(self):
        res = area(10, 3)
        self.assertAlmostEqual(res, 15)

    def test_triangle_area_zero(self):
        res = area(4, 0)
        self.assertEqual(res, 0)

    def test_triangle_area_float(self):
        res = area(2.2, 10.9)
        self.assertAlmostEqual(res, 11.99)

    def test_triangle_area_negative(self):
        res = area(-9, 5)
        self.assertEqual(res, "ERROR")

    def test_triangle_perimetr_zero(self):
        res = perimeter(0, 2, 1)
        self.assertAlmostEqual(res, 3)

    def test_triangle_perimeter_false(self):
        res = perimeter(10, 4,5)
        self.assertEqual(res, "ERROR")

    def test_triangle_perimeter_integer(self):
        res = perimeter(2, 4,3)
        self.assertEqual(res, 9)

    def test_triangle_perimeter_float(self):
        res = perimeter(3.2, 3.9, 4.5)
        self.assertEqual(res, 11.6)

    def test_triangle_perimeter_negative(self):
        res = perimeter(1, 1, -1)
        self.assertEqual(res, "ERROR")

