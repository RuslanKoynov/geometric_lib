import unittest
from square import area
from square import perimeter

class SquareTestCase(unittest.TestCase):
    def test_int(self):
        self.assertEqual(area(5),5*5)
        self.assertEqual(perimeter(12),4*12)
    
    def test_float(self):
        self.assertEqual(area(10.5),10.5*10.5)
        self.assertEqual(perimeter(5.5),4*5.5)