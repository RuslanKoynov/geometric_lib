import unittest

''' Принимает число a и возвращает площадь квадрата '''
def area(a):
    return a * a

''' Принимает число a и возвращает периметр квадрата '''
def perimeter(a):
    return 4 * a

class SquareTestCase(unittest.TestCase):
   def test_area_1(self):
       res = area(4)
       self.assertEqual(res, 16)
   def test_perimeter_1(self):
       res = perimeter(4)
       self.assertEqual(res, 16)

   def test_area_2(self):
       res = area(-4)
       self.assertEqual(res, "a can not be negative")
   def test_perimeter_2(self):
       res = perimeter(-4)
       self.assertEqual(res, "a can not be negative")

   def test_area_3(self):
       res = area(0)
       self.assertEqual(res, 0)
   def test_perimeter_3(self):
       res = perimeter(0)
       self.assertEqual(res, 0)

   def test_area_3(self):
       res = area(4.5)
       self.assertEqual(res, 20.25)
   def test_perimeter_3(self):
       res = perimeter(4.5)
       self.assertEqual(res, 18)
