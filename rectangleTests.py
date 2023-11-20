import unittest
from rectangle import area
from rectangle import perimeter


class CircleTests(unittest.TestCase):

    def test_zero_area(self):
        res = area(0, 123)
        self.assertEqual(res, 0)

    def test_one_area(self):
        res = area(1, 123)
        self.assertEqual(res, 123)

    def test_float_area(self):
        res = area(2.5, 3)
        self.assertEqual(res, 7.5)

    def test_negative_area(self):
        res = area(-5, 2)
        self.assertEqual(res, 10)

    def test_string_area(self):
        res = area("123", 2)
        self.assertEqual(res, 246)


    def test_zero_perimeter(self):
        res = perimeter(0, 123)
        self.assertEqual(res, 0)

    def test_one_perimeter(self):
        res = perimeter(1, 123)
        self.assertEqual(res, 248)

    def test_float_perimeter(self):
        res = perimeter(2.5, 3)
        self.assertEqual(res, 11.0)

    def test_negative_perimeter(self):
        res = perimeter(-5, 2)
        self.assertEqual(res, 6)

    def test_string_perimeter(self):
        res = perimeter("123", 2)
        self.assertEqual(res, 250)