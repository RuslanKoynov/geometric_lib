import unittest

from circle import area
from circle import perimeter

class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)
    def test_square_area(self):
        res = area(11)
        self.assertEqual(res, 380.1327110843649)
    def test_big_numbers_area(self):
        res = area(4294967295)
        self.assertEqual(res, 5.795215563763091e+19)
    def test_string_area(self):
        res = area('python')
        self.assertEqual(res, False)
    def test_negative_area(self):
        res = area(-100)
        self.assertEqual(res, False)
    def test_rational_area(self):
        res = area(0.061)
        self.assertEqual(res, 0.01168986626400762)
        
    def test_zero_peri(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    def test_square_peri(self):
        res = perimeter(11)
        self.assertEqual(res, 69.11503837897544)
    def test_big_numbers_peri(self):
        res = perimeter(4294967295)
        self.assertEqual(res, 26986075402.760853)
    def test_string_peri(self):
        res = perimeter('who')
        self.assertEqual(res, False)
    def test_negative_peri(self):
        res = perimeter(-100)
        self.assertEqual(res, False)
    def test_rational_peri(self):
        res = perimeter(0.061)
        self.assertEqual(res, 0.38327430373795474)
    
    
