import unittest
import triangle
from contextlib import nullcontext as does_not_raise


class TestTriangle(unittest.TestCase):
    def test_area_integer(self):
        res = triangle.area(1, 2)
        excepted = 1

        self.assertEqual(excepted, res)

    def test_area_float(self):
        excepted = 0.001

        self.assertAlmostEqual(excepted, triangle.area(2, 0.001), 6)
        self.assertAlmostEqual(excepted, triangle.area(0.001, 2), 6)

    def test_area_zero_side(self):
        with self.assertRaises(ValueError) as context:
            triangle.area(0, 10)

    def test_area_zero_height(self):
        with self.assertRaises(ValueError) as context:
            triangle.area(10, 0)

    def test_area_negative_side(self):
        with self.assertRaises(ValueError) as context:
            triangle.area(-1, 10)

    def test_area_negative_height(self):
        with self.assertRaises(ValueError) as context:
            triangle.area(10, -1)

    def test_area_string_side(self):
        with self.assertRaises(TypeError) as context:
            triangle.area('ab', 10)

    def test_area_string_height(self):
        with self.assertRaises(TypeError) as context:
            triangle.area(10, 'ab')

    def test_perimeter_integer(self):
        res = triangle.perimeter(10, 20, 25)
        excepted = 6

        self.assertEqual(excepted, res)

    def test_perimeter_float(self):
        self.assertAlmostEqual(7.001, triangle.perimeter(2.001, 2, 3), 6)
        self.assertAlmostEqual(7.001, triangle.perimeter(2, 2.001, 3), 6)
        self.assertAlmostEqual(7.001, triangle.perimeter(2, 3, 2.001), 6)

    def test_perimeter_irregular_triangle(self):
        with self.assertRaises(ValueError) as context:
            triangle.perimeter(10, 20, 30)

    def test_perimeter_side_one_string(self):
        with self.assertRaises(TypeError) as context:
            triangle.perimeter('ab', 20, 30)

    def test_perimeter_side_two_string(self):
        with self.assertRaises(TypeError) as context:
            triangle.perimeter(10, 'ab', 30)

    def test_perimeter_side_three_string(self):
        with self.assertRaises(TypeError) as context:
            triangle.perimeter(10, 20, 'ab')
