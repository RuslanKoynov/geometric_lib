import unittest
import triangle

class TestTriangleCase(unittest.TestCase):
    def test_positive_area(self):
        res = triangle.area(10, 6)
        self.assertEqual(res, 30)

    def test_zero_area(self):
        with self.assertRaises(ValueError):
            res = triangle.area(0)

    def test_negative_side_triangle_area(self):
        with self.assertRaises(ValueError):
            res = triangle.area(0)

    def test_positive_perimeter(self):
        res = triangle.perimeter(10, 5, 8)
        self.assertEqual(res, 23)

    def test_zero_perimetr(self):
        with self.assertRaises(ValueError):
            res = triangle.perimetr(0)

    def test_negative_side_triangle_perimetr(self):
        with self.assertRaises(ValueError):
            res = triangle.perimetr(0)
