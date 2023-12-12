import unittest

from rectangle import area
from rectangle import perimeter


class MyTestCase(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(4, 3), (4 * 3))

    def test_area_errorValue(self):
        self.assertRaises(ValueError, area, (-1, 2))

    def test_area_typeError(self):
        self.assertRaises(TypeError, area, "abcd")

    def test_perimeter(self):
        self.assertEqual(perimeter(4, 3), (4 + 3)*2)

    def test_perimeter_errorValue(self):
        self.assertRaises(ValueError, perimeter, (-1, 2))

    def test_perimeter_typeError(self):
        self.assertRaises(TypeError, perimeter, "abcd")