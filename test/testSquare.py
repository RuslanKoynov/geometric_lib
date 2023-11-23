import unittest
import os
import sys 
sys.path.insert(1, os.path.join(sys.path[0], "..")) 
from square import *
class RectangleTestCase(unittest.TestCase):
    def test_area_zero_value(self):
        res = area(0)
        self.assertEqual(res, 0)
        
    def test_area_positive_value(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_perimeter_zero_radius(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
        
    def test_perimeter_positive_value(self):
        res = perimeter(10)
        self.assertEqual(res, 40)


if __name__ == '__main__':
    unittest.main()