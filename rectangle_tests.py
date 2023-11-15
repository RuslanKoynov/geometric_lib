import unittest
from rectangle import area
from rectangle import perimeter
from math import pi

class RecrangleTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(2, 2), 2*2)
        self.assertEqual(area(3, 1.5), 3*(1.5))
        self.assertEqual(area(3,5), 3*5)
        self.assertEqual(area(5,3), 5*3)
        self.assertEqual(area(2.3, 4.6), (2.3)*(4.6))
    def test_values(self):
        self.assertRaises(ValueError, area, 1, 0)
        self.assertRaises(ValueError, area, -7, 2)
        self.assertRaises(ValueError, area, -8, -9)
    def test_types(self):
        self.assertRaises(TypeError, area, 3+4j, 1+3j)
        self.assertRaises(TypeError, area, 'two', 'four')
        self.assertRaises(TypeError, area, [5], [4])
        self.assertRaises(TypeError, area, {3,5}, {4,7})

    def test_perimeter(self):
        self.assertEqual(perimeter(2, 2), 2*2 + 2*2)
        self.assertEqual(perimeter(3, 1.5), 2*3 + 2*(1.5))
        self.assertEqual(perimeter(3,5), 2*3 + 2*5)
        self.assertEqual(perimeter(5,3), 2*5 + 2*3)
        self.assertEqual(perimeter(2.3, 4.6), 2*(2.3) + 2*(4.6))
    def test_values(self):
        self.assertRaises(ValueError, perimeter, 1, 0)
        self.assertRaises(ValueError, perimeter, -7, 2)
        self.assertRaises(ValueError, perimeter, -8, -9)
    def test_types(self):
        self.assertRaises(TypeError, perimeter, 3+4j, 1+3j)
        self.assertRaises(TypeError, perimeter, 'two', 'four')
        self.assertRaises(TypeError, perimeter, [5], [4])
        self.assertRaises(TypeError, perimeter, {3,5}, {4,7})