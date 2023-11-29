import unittest
from triangle import area
from triangle import perimeter
class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
       res = area(10, 0)
       self.assertEqual(res, 0)
       
    def test_square_mul(self):
       res = area(10, 10)
       self.assertEqual(res, 50)

    def test_perimeter(self):
       res = perimeter(10,5,100)
       self.assertEqual(res, 115)
