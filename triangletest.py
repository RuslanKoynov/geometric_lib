import unittest
from triangle import area
from triangle import perimeter

class TriangleTestCase(unittest.TestCase):
    def test_int(self):
        self.assertEqual(area(5,7),5*7/2)
        self.assertEqual(perimeter(19,4,3),19+4+3)
    
    def test_float(self):
        self.assertEqual(area(10.5,12.5),10.5*12.5/2)
        self.assertEqual(perimeter(5.5,6.7,98.5),5.5+6.7+98.5)
        
    def test_int_and_float(self):
        self.assertEqual(area(6,12.5),6*12.5/2)
        self.assertEqual(perimeter(55,67,98.5),55+67+98.5)