import unittest
from rectangle import area, perimeter
class RectangleTestCase(unittest.TestCase):
##    def setUp(self):
        
    
   def test_zero_mul(self):
       res = area(10, 0)
       self.assertEqual(res, 0)
       
   def test_square_mul(self):
       res = area(10, 10)
       self.assertEqual(res, 100)
       
    def test_perimeter(self):
       res = perimeter(10, 5)
       self.assertEqual(res, 30)


  
















       
