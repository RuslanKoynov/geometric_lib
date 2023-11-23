import unittest
import triangle

class TestTriangleCase(unittest.TestCase):
    def test_positive_area(self):
        res = triangle.area(12, 6)
        self.assertEqual(res, 36)

    def test_zero_area(self):
        res = triangle.area(0, 5)
        self.assertEqual(res, 0)

    def test_negative_area(self):
        res = area(4, -5)
        self.assertEqual(res, 0)

    def test_positive_perimeter(self):
        res = triangle.perimeter(15, 5, 8)
        self.assertEqual(res, 28)

    def test_zero_perimetr(self):
        res = triangle.perimeter(5, 9, 0)
        self.assertEqual(res, 0)

    def test_negative_perimetr(self):
        res = perimeter(4, 9, -6)
        self.assertEqual(res, 0)
