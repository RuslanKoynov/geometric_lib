from square import area,perimeter
import unittest

class SquareTestCase(unittest.TestCase):

    def test_area_positive(self):
        res = area(11)
        self.assertEqual(res, 121)

    def test_area_negative(self):
            with self.assertRaises(Exception):
                area(-5)

    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0.0)

    def test_area_real(self):
        res = area(54.23)
        self.assertEqual(res, 2940.8929)

    def test_perimeter_positive(self):
        res = perimeter(123)
        self.assertEqual(res, 492)

    def test_perimeter_negative(self):
            with self.assertRaises(Exception):
                perimeter(-234)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0.0)

    def test_perimeter_real(self):
        res = perimeter(324.123)
        self.assertEqual(res, 1296.492)
