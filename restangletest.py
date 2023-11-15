import unittest
from rectangle import area
from rectangle import perimeter

class RectangleTestCase(unittest.TestCase):
    def test_int(self):
        self.assertEqual(area(51,27),51*27)
        self.assertEqual(area(43,7),43*7)
        self.assertEqual(perimeter(19,4),2*(19+4))
        self.assertEqual(perimeter(65,49),2*(65+49))
    
    def test_float(self):
        self.assertEqual(area(13.7,12.5),13.7*12.5)
        self.assertEqual(area(43.81,54.67),43.81*54.67)
        self.assertEqual(perimeter(5.5,6.7),2*(5.5+6.7))
        self.assertEqual(perimeter(12.74,52.8),2*(12.74+52.8))
        
    def test_int_and_float(self):
        self.assertEqual(area(4,12.8),4*12.8)
        self.assertEqual(area(32.9,76),32.9*76)
        self.assertEqual(perimeter(5,98.5),2*(5+98.5))
        self.assertEqual(perimeter(81.5,369),2*(81.5+369))
