import unittest
import os
import sys 
sys.path.insert(1, os.path.join(sys.path[0], "..")) 
from triangle import *
class RectangleTestCase(unittest.TestCase):
    def test_area_zero_value(self):
        res = area(10, 0)
        self.assertEqual(res, 0)
        
    def test_area_positive_values(self):
        res = area(10,10)
        self.assertEqual(res, 50)

    def test_perimeter_zero_value(self):
        res = perimeter(10, 10, 0)
        self.assertEqual(res, 20)
        
    def test_perimeter_positive_values(self):
        res = perimeter(10, 20, 30)
        self.assertEqual(res, 60)


if __name__ == '__main__':
    unittest.main()