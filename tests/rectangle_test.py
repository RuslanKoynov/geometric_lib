import unittest

from rectangle import area
from rectangle import perimeter

class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0, 561892640)
        self.assertEqual(res, 0)
    def test_square_area(self):
        res = area(33, 33)
        self.assertEqual(res, 1089)
    def test_big_numbers_area(self):
        res = area(4294967295, 4294967295)
        self.assertEqual(res, 18446744065119617025)
    def test_string_area(self):
        res = area('hello', 1234)
        self.assertEqual(res, False)
    def test_negative_area(self):
        res = area(-100, 22)
        self.assertEqual(res, False)
    def test_rational_area(self):
        res = area(12.2, 0.5)
        self.assertEqual(res, 6.1)
        
    def test_zero_peri(self):
        res = perimeter(0, 561892641)
        self.assertEqual(res, 1123785282)
    def test_square_peri(self):
        res = perimeter(22, 22)
        self.assertEqual(res, 88)
    def test_big_numbers_peri(self):
        res = perimeter(4294967295, 429496729)
        self.assertEqual(res, 9448928048)
    def test_string_peri(self):
        res = perimeter('fish', 1234)
        self.assertEqual(res, False)
    def test_negative_peri(self):
        res = perimeter(-100,23)
        self.assertEqual(res, False)
    def test_rational_peri(self):
        res = perimeter(12.2, 0.5)
        self.assertEqual(res,25.4)
    
    
