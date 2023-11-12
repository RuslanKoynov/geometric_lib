import unittest

import square

class SquareAreaTestCase(unittest.TestCase):
    def test_simple(self):
        res = square.area(3)
        self.assertEqual(res, 9)
    
    def test_negative_side(self):
        res = square.area(-3)
        self.assertEqual(res, 0)

    def test_zero_side(self):
        res = square.area(0)
        self.assertEqual(res, 0)

class SquarePerimeterTestCase(unittest.TestCase):
    def test_simple(self):
        res = square.perimeter(3)
        self.assertEqual(res, 12)
    
    def test_negative_side(self):
        res = square.perimeter(-3)
        self.assertEqual(res, 0)

    def test_zero_side(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)
