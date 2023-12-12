import unittest

from square import area
from square import perimeter


class MyTestCase(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(4), 4 ** 2)

    def test_area_errorValue(self):
        self.assertRaises(ValueError, area, -12345)

    def test_area_typeError(self):
        self.assertRaises(TypeError, area, "abcd")

    def test_perimeter(self):
        self.assertEqual(perimeter(4), 4 * 4)

    def test_perimeter_errorValue(self):
        self.assertRaises(ValueError, perimeter, -12345)

    def test_perimeter_typeError(self):
        self.assertRaises(TypeError, perimeter, "abcd")