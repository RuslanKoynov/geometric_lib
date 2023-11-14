import unittest
from circle import area
from circle import perimeter
from math import pi

class CircleTestCase(unittest.TestCase):
    def test_int(self):
        self.assertEqual(area(1),pi)
        self.assertEqual(perimeter(10),2*pi*10)
    
    def test_float(self):
        self.assertEqual(area(1.5),pi*1.5**2)
        self.assertEqual(perimeter(3.5),2*pi*3.5)