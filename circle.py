import math
import unittest
def area(r):
    return math.pi * r * r
def perimeter(r):
    return 2 * math.pi * r
class SquareTestCase(unittest.TestCase):
   def test_zero_mul(self):
       res = area(0)
       self.assertEqual(res, 0)
   def test_curcle_mul(self):
       res = area(6)
       self.assertEqual(res, 113.09733552923255)

   def test_zero_per(self):
       res = perimeter(0)
       self.assertEqual(res, 0)

   def test_circle_per(self):
       res = perimeter(6)
       self.assertEqual(res, 37.69911184307752)

