import unittest
from rectangle import area
from rectangle import perimeter

class RectangleTestCase(unittest.TestCase):
    def test_rectangle_area_positive(self):
        res = area(5, 8)
        self.assertEqual(res, 40)

    def test_rectangle_area_real(self):
        res = area(5.5, 9.9)
        self.assertEqual(res, 54.45)

    def test_rectangle_area_zero(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_rectangle_perimeter_positive(self):
        res = perimeter(5, 7)
        self.assertEqual(res, 24)

    def test_rectangle_perimeter_real(self):
        res = perimeter(5.5, 6.6)
        self.assertEqual(res, 24.2)

    def test_rectangle_perimeter_zero(self):
        res =  perimeter(5, 0)
        self.assertEqual(res, 10)
