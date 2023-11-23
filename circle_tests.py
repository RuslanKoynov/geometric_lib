import math
from circle import area
from circle import perimeter
import unittest


class CircleTestCase(unittest.TestCase):
    def test_area_positive(self):
        res = area(6)
        self.assertEqual(res, 113.04)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            res = perimeter(-10)

    def test_area_real(self):
        res = area(4.5)
        self.assertEqual(res, 63.585)

    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_perimeter_positive(self):
        res = perimeter(6)
        self.assertEqual(res, 37.68)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            res = perimeter(-10)

    def test_perimeter_real(self):
        res = perimeter(4.5)
        self.assertEqual(res, 28.26)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)


if __name__ == '__main__':
    unittest.main()
