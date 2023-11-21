import unittest
from circle import area, perimeter
class CircleTestCase(unittest.TestCase):
    def test_circle_area(self):
        res = area(8)
        self.assertEqual(res, 201.06192982974676)

    def test_circle_area_negative(self):
        res = area(-1)
        self.assertEqual(res, "ERROR")
    def test_circle_area_2(self):
        res = area(44)
        self.assertEqual(res, 6082.123377349839)

    def test_circle_area_null(self):
        res = area(0)
        self.assertEqual(res, 0.0)

    def test_circle_perimetr(self):
        res = perimeter(6)
        self.assertEqual(res, 37.69911184307752)

    def test_circle_perimetr_negative(self):
        res = perimeter(-1)
        self.assertEqual(res, "ERROR")

    def test_circle_perimetr_2(self):
        res = perimeter(31)
        self.assertEqual(res, 194.77874452256717)

    def test_circle_perimeter_null(self):
        res = perimeter(0)
        self.assertEqual(res, 0.0)
