import unittest

from triangle import area
from triangle import perimeter


class MyTestCase(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(4, 3), (4 * 3) / 2)

    def test_area_errorValue(self):
        self.assertRaises(ValueError, area, (-5, 3))

    def test_area_TypeError(self):
        self.assertRaises(TypeError, area,  "abcd")

    def test_perimeter(self):
        self.assertEqual(perimeter(1, 5, 7), (1 + 5 + 7))

    def test_perimeter_errorValue(self):
        self.assertRaises(ValueError, perimeter, (-5, 3))

    def test_perimeter_TypeError(self):
        self.assertRaises(TypeError, perimeter, "abcd")