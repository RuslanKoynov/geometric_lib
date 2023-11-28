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

    def test_perimetr_null(self):
        res = perimeter(5, 5, 0)
        self.assertEqual(res, 25)

    def test_perimetr_normal(self):
        res = perimeter(5, 10, 12)
        self.assertEqual(res, 27)
