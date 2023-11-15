import unittest

from triangle import area
from triangle import perimeter

class TriangleTestCase(unittest.TestCase):
    def test_area_null(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_area_normal(self):
        res = area(10, 10)
        self.assertEqual(res, 10)

    def test_area_negative(self):
        res = area(5, -3)
        self.assertEqual(res, "false")

    def test_perimetr_null(self):
        res = perimeter(5, 3, 0)
        self.assertEqual(res, "false")

    def test_perimetr_normal(self):
        res = perimeter(5, 10, 12)
        self.assertEqual(res, 27)

    def test_perimetr_negative(self):
        res = perimeter(5, 10, -5)
        self.assertEqual(res, "false")