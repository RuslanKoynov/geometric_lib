import unittest
def area(a, b): 
    return a * b
def perimeter(a, b): 
    return (a + b)*2
class RectangleTestCase(unittest.TestCase):
   def test_zero_mul(self):
       res = area(10, 0)
       self.assertEqual(res, 0)
   def test_rectangle_mul(self):
       res = area(10, 10)
       self.assertEqual(res, 100)

   def test_zero_per(self):
       res = perimeter(10, 0)
       self.assertEqual(res, 20)

   def test_rectangle_per(self):
       res = perimeter(10, 15)
       self.assertEqual(res, 50)

