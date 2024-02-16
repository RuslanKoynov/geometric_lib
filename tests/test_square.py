import unittest
import square


class TestSquare(unittest.TestCase):
    def test_area_integer(self):
        res = square.area(5)
        excepted = 25

        self.assertEqual(excepted, res)

    def test_area_float(self):
        excepted = 0.0025

        self.assertAlmostEqual(excepted, square.area(0.05), 6)

    def test_area_zero_side(self):
        with self.assertRaises(ValueError) as context:
            square.area(0)

    def test_area_negative_side(self):
        with self.assertRaises(ValueError) as context:
            square.area(-1)

    def test_area_string_side(self):
        with self.assertRaises(TypeError) as context:
            square.area('ab')

    def test_perimeter_integer(self):
        res = square.perimeter(5)
        excepted = 20

        self.assertEqual(excepted, res)

    def test_perimeter_float(self):
        excepted = 0.2

        self.assertAlmostEqual(excepted, square.perimeter(0.05), 6)

    def test_perimeter_zero_side(self):
        with self.assertRaises(ValueError) as context:
            square.perimeter(0)

    def test_perimeter_negative_side(self):
        with self.assertRaises(ValueError) as context:
            square.perimeter(-1)

    def test_perimeter_string_side(self):
        with self.assertRaises(TypeError) as context:
            square.perimeter('ab')
