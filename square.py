import unittest
def area(a):
    return a * a
def perimeter(a):
    return 4 * a
class SquareTestCase(unittest.TestCase):
   def test_zero_mul(self):
       res = area(0)
       self.assertEqual(res, 0)
   def test_square_mul(self):
       res = area(9)
       self.assertEqual(res, 81)

   def test_zero_per(self):
       res = perimeter(0)
       self.assertEqual(res, 0)

   def test_square_per(self):
       res = perimeter(9)
       self.assertEqual(res, 36)

