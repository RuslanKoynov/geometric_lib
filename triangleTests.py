import unittest
from triangle import area
from triangle import perimeter


class CircleTests(unittest.TestCase):

    def test_zero_area(self):
        res = area(0, 2)
        self.assertEqual(res, 0)

    def test_one_area(self):
        res = area(1, 2)
        self.assertEqual(res, 1)

    def test_float_area(self):
        res = area(2.5, 2)
        self.assertEqual(res, 2.5)

    def test_negative_area(self):
        res = area(-5, 10)
        self.assertEqual(res, 25)

    def test_string_area(self):
        res = area("123", 2)
        self.assertEqual(res, 123)


    def test_zero_perimeter(self):
        res = perimeter(0, 1, 2)
        self.assertEqual(res, 0)

    def test_one_perimeter(self):
        res = perimeter(1, 2, 3)
        self.assertEqual(res, 6)

    def test_float_perimeter(self):
        res = perimeter(2.5, 2.5, 2.5)
        self.assertEqual(res, 7.5)

    def test_negative_perimeter(self):
        res = perimeter(-5, -1, -4)
        self.assertEqual(res, 10)

    def test_string_perimeter(self):
        res = perimeter("123", "1", "2")
        self.assertEqual(res, 126)