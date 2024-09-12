import unittest

from square import area
from square import perimeter

class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)
    def test_square_area(self):
        res = area(33)
        self.assertEqual(res, 1089)
    def test_big_numbers_area(self):
        res = area(4294967295)
        self.assertEqual(res, 18446744065119617025)
    def test_string_area(self):
        res = area('nice')
        self.assertEqual(res, False)
    def test_negative_area(self):
        res = area(-100)
        self.assertEqual(res, False)
    def test_rational_area(self):
        res = area(0.03)
        self.assertEqual(res, 0.0009)
        
    def test_zero_peri(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    def test_square_peri(self):
        res = perimeter(22)
        self.assertEqual(res, 88)
    def test_big_numbers_peri(self):
        res = perimeter(4294967296)
        self.assertEqual(res, 17179869184)
    def test_string_peri(self):
        res = perimeter('what')
        self.assertEqual(res, False)
    def test_negative_peri(self):
        res = perimeter(-100)
        self.assertEqual(res, False)
    def test_rational_peri(self):
        res = perimeter(12.2)
        self.assertEqual(res,48.8)
    
    
