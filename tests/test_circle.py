import unittest
import circle


class TestCircle(unittest.TestCase):
    def test_area_integer(self):
        res = circle.area(1234)
        excepted = 4783879.062809778

        self.assertAlmostEqual(excepted, res, 6)

    def test_area_float(self):
        eps = 0.1 ** 10
        res = circle.area(0.001)
        excepted = 0.0000031415927

        self.assertAlmostEqual(excepted, res, 6)

    def test_area_zero(self):
        with self.assertRaises(ValueError) as context:
            circle.area(0)

    def test_area_negative(self):
        with self.assertRaises(ValueError) as context:
            circle.area(-1)

    def test_area_string(self):
        with self.assertRaises(TypeError) as context:
            circle.area('ab')

    def test_perimeter_integer(self):
        res = circle.perimeter(1234)
        excepted = 7753.4506690596

        self.assertAlmostEqual(excepted, res, 6)

    def test_perimeter_float(self):
        res = circle.perimeter(0.001)
        excepted = 0.0062831853072

        self.assertAlmostEqual(excepted, res, 6)

    def test_perimeter_zero(self):
        with self.assertRaises(ValueError) as context:
            circle.perimeter(0)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError) as context:
            circle.perimeter(-1)

    def test_perimeter_string(self):
        with self.assertRaises(TypeError) as context:
            circle.perimeter('ab')
