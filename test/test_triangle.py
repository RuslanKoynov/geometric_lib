import unittest
import math

import triangle

class TriangleAreaTestCase(unittest.TestCase):
    def test_simple(self):
        res = triangle.area(3, 4)
        self.assertEqual(res, 6)

    def test_zero_side(self):
        res = triangle.area(0, 3)
        self.assertEqual(res, 0)
    
    def test_zero_height(self):
        res = triangle.area(3, 0)
        self.assertEqual(res, 0)
    
    def test_negative_side(self):
        res = triangle.area(-3, 4)
        self.assertEqual(res, 0)
    
    def test_negative_height(self):
        res = triangle.area(3, -4)
        self.assertEqual(res, 0)

class TrianglePerimeterTestCase(unittest.TestCase):
    def test_simple(self):
        res = triangle.perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_zero_side(self):
        res = triangle.perimeter(0, 4, 5)
        self.assertEqual(res, 0)
    
    def test_negative_side(self):
        res = triangle.perimeter(-3, 4, 5)
        self.assertEqual(res, 0)

class TriangleMedianTestCase(unittest.TestCase):
    def test_simple(self):
        res = triangle.median(3, 4, 5)
        self.assertEqual(res, math.sqrt(2 * 25 + 2 * 16 - 9) / 2)
    
    def test_negative_first_side(self):
        res = triangle.median(-3, 4, 5)
        self.assertEqual(res, 0)
    
    def test_negative_second_side(self):
        res = triangle.median(3, -4, 5)
        self.assertEqual(res, 0)
    
    def test_zero_first_side(self):
        res = triangle.median(0, 4, 5)
        self.assertEqual(res, 0)
    
    def test_zero_second_side(self):
        res = triangle.median(3, 0, 5)
        self.assertEqual(res, 0)
