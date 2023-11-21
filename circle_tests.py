import unittest
from circle import area, perimeter
import math
class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(8)
        self.assertEqual(res, 201.06192982974676)

    def test_circle_mul(self):
        res = area(-1)
        self.assertEqual(res, "ERROR")
    def test_area_zero(self):
        res = area(44)
        self.assertEqual(res, 6082.123377349839)

    def test_circle_mul(self):
        res = area(0)
        self.assertEqual(res, 0.0)

    def test_perimetr_mul(self):
        res = area(6)
        self.assertEqual(res, 37.69911184307752)

    def test_circle_mul(self):
        res = perimeter(-1)
        self.assertEqual(res, "ERROR")

    def test_perimetr_mul(self):
        res = area(31)
        self.assertEqual(res, 194.77874452256717)

    def test_circle_mul(self):
        res = perimeter(0)
        self.assertEqual(res, 0.0)


if  __name__ == "__main__":
    unittest.main()

