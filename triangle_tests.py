from triangle import area, perimeter
import unittest

class TriangleTestCase(unittest.TestCase):
    def test_triangle_area(self):
        res = area(10, 3)
        self.assertEqual(res, 15)

    def test_triangle_area_2(self):
        res = area(4, 2)
        self.assertEqual(res, 4)

    def test_triangle_area_3(self):
        res = area(50, 10)
        self.assertEqual(res, 250)

    def test_triangle_area_negative(self):
        res = area(-9, 5)
        self.assertEqual(res, "ERROR")

    def test_triangle_perimeter_false(self):
        res = perimeter(10, 4,5)
        self.assertEqual(res, "ERROR")

    def test_triangle_perimeter(self):
        res = perimeter(2, 4,3)
        self.assertEqual(res, 9)

    def test_triangle_perimeter_2(self):
        res = perimeter(30, 36, 22)
        self.assertEqual(res, 88)

    def test_triangle_perimeter_negative(self):
        res = perimeter(1, 1, -1)
        self.assertEqual(res, "ERROR")

