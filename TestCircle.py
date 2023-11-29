import unittest
import math
from circle import area
from circle import perimetr
class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
       res = area(0)
       self.assertEqual(res, 0.0)
       
    def test_area(self):
       res = area(10)
       self.assertEqual(res, 314.1592653589793)

    def test_perimeter(self):
       res = perimeter(7)
       self.assertEqual(res, 43.982297150257104)
//