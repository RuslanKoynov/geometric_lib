import unittest

from triangle import area
from triangle import perimeter

class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0, 566401892)
        self.assertEqual(res, 0)
    def test_square_area(self):
        res = area(123, 54)
        self.assertEqual(res, 3321)
    def test_big_numbers_area(self):
        res = area(4294967295, 4294295)
        self.assertEqual(res, 9221928290041012.0)
    def test_string_area(self):
        res = area('wow', 41)
        self.assertEqual(res, False)
    def test_negative_area(self):
        res = area(22, -100)
        self.assertEqual(res, False)
    def test_rational_area(self):
        res = area(53.1, 5.3)
        self.assertEqual(res, 140.715)
        
    def test_zero_peri(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)
    def test_square_peri(self):
        res = perimeter(5,3,4)
        self.assertEqual(res, 12)
    def test_big_numbers_peri(self):
        res = perimeter(4294967295, 429496729, 42949652729)
        self.assertEqual(res, 47674116753)
    def test_string_peri(self):
        res = perimeter('goingstrong', 70, 'still')
        self.assertEqual(res, False)
    def test_negative_peri(self):
        res = perimeter(-100,23, -1351351)
        self.assertEqual(res, False)
    def test_rational_peri(self):
        res = perimeter(1.2 , 1.3, 1.4)
        self.assertEqual(res, 3.9)
    
    
