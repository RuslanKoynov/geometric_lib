import unittest

import rectangle

class RectangleAreaTestCase(unittest.TestCase):
    def test_simple(self):
        res = rectangle.area(3, 4)
        self.assertEqual(res, 12)
    
    def test_negative_side(self):
        res = rectangle.area(-3, 4)
        self.assertEqual(res, 0)

    def test_zero_side(self):
        res = rectangle.area(0, 1)
        self.assertEqual(res, 0)

class RectanglePerimeterTestCase(unittest.TestCase):
    def test_simple(self):
        res = rectangle.perimeter(3, 4)
        self.assertEqual(res, 14)
    
    def test_negative_side(self):
        res = rectangle.perimeter(-3, 4)
        self.assertEqual(res, 0)

    def test_zero_side(self):
        res = rectangle.perimeter(0, 1)
        self.assertEqual(res, 2)
