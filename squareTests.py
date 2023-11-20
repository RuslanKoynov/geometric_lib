import unittest
from square import area
from square import perimeter


class CircleTests(unittest.TestCase):

    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_one_area(self):
        res = area(1)
        self.assertEqual(res, 1)

    def test_float_area(self):
        res = area(2.5)
        self.assertEqual(res, 6.25)

    def test_negative_area(self):
        res = area(-5)
        self.assertEqual(res, 25)

    def test_string_area(self):
        res = area("123")
        self.assertEqual(res, 15129)


    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_one_perimeter(self):
        res = perimeter(1)
        self.assertEqual(res, 4)

    def test_float_perimeter(self):
        res = perimeter(2.5)
        self.assertEqual(res, 10)

    def test_negative_perimeter(self):
        res = perimeter(-5)
        self.assertEqual(res, 20)

    def test_string_perimeter(self):
        res = perimeter("123")
        self.assertEqual(res, 492)