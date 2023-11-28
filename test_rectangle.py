import unittest

from rectangle import area
from rectangle import perimeter

class RectangleTestCase(unittest.TestCase):
    def test_rectangle_nul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_rectangle_normal(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_rectangle_perimetr_nul(self):
        res = perimeter(10, 0)
        self.assertEqual(res, 20)

    def test_rectangle_normal(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)


