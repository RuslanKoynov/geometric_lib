import unittest

from circle import area
from circle import perimeter
from math import pi


class MyTestCase(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(4), pi * 4 ** 2)

    def test_area_errorValue(self):
        self.assertRaises(ValueError, area, -12345)

    def test_area_errorType(self):
        self.assertRaises(TypeError, area, "abcd")

    def test_perimetr(self):
        self.assertEqual(perimeter(4), pi * 4 * 2)

    def test_perimetr_errorValue(self):
        self.assertRaises(ValueError, perimeter, -12345)

    def test_perimetr_errorType(self):
        self.assertRaises(TypeError, perimeter, "abcd")