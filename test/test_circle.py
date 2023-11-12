import unittest
import math

import circle

class CircleAreaTestCase(unittest.TestCase):
    def test_simple(self):
        res = circle.area(3)
        self.assertEqual(res, 9 * math.pi)
    
    def test_zero_radius(self):
        res = circle.area(0)
        self.assertEqual(res, 0)
    
    def test_negative_radius(self):
        res = circle.area(-1)
        self.assertEqual(res, 0)

class CirclePerimeterTestCase(unittest.TestCase):
    def test_simple(self):
        res = circle.perimeter(3)
        self.assertEqual(res, 6 * math.pi)
    
    def test_negative_radius(self):
        res = circle.perimeter(-1)
        self.assertEqual(res, 0)
    
    def test_zero_radius(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)
