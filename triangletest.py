import unittest
from triangle import area
from triangle import perimeter

class TriangleTestCase(unittest.TestCase):
    def test_int(self):
        self.assertEqual(area(5,7),5*7/2)
        self.assertEqual(area(43,2),43*2/2)
        self.assertEqual(perimeter(19,4,3),19+4+3)
        self.assertEqual(perimeter(1,65,89),1+65+89)
    
    def test_float(self):
        self.assertEqual(area(10.5,12.5),10.5*12.5/2)
        self.assertEqual(area(34.67,44.9),34.67*44.9/2)
        self.assertEqual(perimeter(5.5,6.7,98.5),5.5+6.7+98.5)
        self.assertEqual(perimeter(32,897,65),32+897+65)
        
    def test_int_and_float(self):
        self.assertEqual(area(6,12.5),6*12.5/2)
        self.assertEqual(area(23.7,8),23.7*8/2)
        self.assertEqual(perimeter(55,67,98.5),55+67+98.5)
        self.assertEqual(perimeter(53.89,54,1.2),53.89+54+1.2)