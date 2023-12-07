from square import area, perimeter
import unittest

class SquareTestCase(unittest.TestCase):
    def test_square_area_integer(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_square_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_square_area_float(self):
        res = area(8.69)
        self.assertAlmostEqual(res, 75.51, places=1)
    def test_square_area_negative(self):
        with self.assertRaises(Exception):
            area(-8)

    def test_square_perimeter(self):
        res = perimeter(11)
        self.assertEqual(res, 44)

    def test_square_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_square_perimeter_float(self):
        res = perimeter(3.33)
        self.assertEqual(res, 13.32)

    def test_square_perimeter_negative(self):
        with self.assertRaises(Exception):
            perimeter(-99)
