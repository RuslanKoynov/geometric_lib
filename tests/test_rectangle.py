import unittest
import rectangle


class TestRectangle(unittest.TestCase):
    def test_area_integer(self):
        res = rectangle.area(1, 2)
        excepted = 2

        self.assertEqual(excepted, res)

    def test_area_float(self):
        excepted = 0.002

        self.assertAlmostEqual(excepted, rectangle.area(2, 0.001), 6)
        self.assertAlmostEqual(excepted, rectangle.area(0.001, 2), 6)

    def test_area_zero_side_one(self):
        with self.assertRaises(ValueError) as context:
            rectangle.area(0, 10)

    def test_area_zero_side_two(self):
        with self.assertRaises(ValueError) as context:
            rectangle.area(10, 0)

    def test_area_negative_side_one(self):
        with self.assertRaises(ValueError) as context:
            rectangle.area(-1, 10)

    def test_area_negative_side_two(self):
        with self.assertRaises(ValueError) as context:
            rectangle.area(10, -1)

    def test_area_string_side_one(self):
        with self.assertRaises(TypeError) as context:
            rectangle.area('ab', 10)

    def test_area_string_side_two(self):
        with self.assertRaises(TypeError) as context:
            rectangle.area(10, 'ab')

    def test_perimeter_integer(self):
        res = rectangle.perimeter(1, 2)
        excepted = 3

        self.assertEqual(excepted, res)

    def test_perimeter_float(self):
        excepted = 2.001

        self.assertAlmostEqual(excepted, rectangle.perimeter(2, 0.001), 6)
        self.assertAlmostEqual(excepted, rectangle.perimeter(0.001, 2), 6)

    def test_perimeter_zero_side_one(self):
        with self.assertRaises(ValueError) as context:
            rectangle.perimeter(0, 10)

    def test_perimeter_zero_side_two(self):
        with self.assertRaises(ValueError) as context:
            rectangle.perimeter(10, 0)

    def test_perimeter_negative_side_one(self):
        with self.assertRaises(ValueError) as context:
            rectangle.perimeter(-1, 10)

    def test_perimeter_negative_side_two(self):
        with self.assertRaises(ValueError) as context:
            rectangle.perimeter(10, -1)

    def test_perimeter_string_side_one(self):
        with self.assertRaises(TypeError) as context:
            rectangle.perimeter('ab', 10)

    def test_perimeter_string_side_two(self):
        with self.assertRaises(TypeError) as context:
            rectangle.perimeter(10, 'ab')
