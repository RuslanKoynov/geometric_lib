from rectangle import area, perimeter
import unittest

class RectangleTestCase(unittest.TestCase):
    def test_rectangle_area_zero(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_rectangle_area_integer(self):
        res = area(6, 11)
        self.assertEqual(res, 66)

    def test_rectangle_area_negative(self):
        res = area(-3, 5)
        self.assertEqual(res, "ERROR")

    def test_rectangle_area_float(self):
        res = area(90.22, 1.5)
        self.assertAlmostEqual(res, 135.33, places=2)

    def test_rectangle_perimeter_integer(self):
        res = perimeter(10, 1)
        self.assertEqual(res, 22)

    def test_rectangle_perimeter_zero(self):
        res = perimeter(0, 20)
        self.assertEqual(res, 40)

    def test_rectangle_perimeter_float(self):
        res = perimeter(2.1,5.5)
        self.assertEqual(res, 15.2)

    def test_rectangle_perimeter_negative(self):
        res = perimeter(-4, 9)
        self.assertEqual(res, "ERROR")



