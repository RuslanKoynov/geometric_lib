import unittest
from rectangle import area
from rectangle import perimeter

class RectangleTestCase(unittest.TestCase):
    def test_int(self):
        self.assertEqual(area(51,27),51*27)
        self.assertEqual(perimeter(19,4),2*(19+4))
    
    def test_float(self):
        self.assertEqual(area(13.7,12.5),13.7*12.5)
        self.assertEqual(perimeter(5.5,6.7),2*(5.5+6.7))
        
    def test_int_and_float(self):
        self.assertEqual(area(4,12.8),4*12.8)
        self.assertEqual(perimeter(5,98.5),2*(5+98.5))
