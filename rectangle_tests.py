from rectangle import area, perimeter
import unittest

class RectangleTestCase(unittest.TestCase):
    def test_rectangle_area_zero(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_rectangle_area(self):
        res = area(6, 11)
        self.assertEqual(res, 66)

    def test_rectangle_area_negative(self):
        res = area(-3, 5)
        self.assertEqual(res, "ERROR")

    def test_rectangle_area_2(self):
        res = area(90, 1)
        self.assertEqual(res, 90)

    def test_rectangle_perimeter(self):
        res = perimeter(10, 1)
        self.assertEqual(res, 22)

    def test_rectangle_perimeter_2(self):
        res = perimeter(10, 20)
        self.assertEqual(res, 60)

    def test_rectangle_perimeter_3(self):
        res = perimeter(2, 3)
        self.assertEqual(res, 10)

    def test_rectangle_perimeter_negative(self):
        res = perimeter(-4, 9)
        self.assertEqual(res, "ERROR")