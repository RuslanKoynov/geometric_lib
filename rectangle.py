import unittest

''' Принимает числа a, b и возвращает площадь стороны a и b '''
def area(a, b):
    return a * b

''' Принимает числа a, b и возвращает периметр стороны a и b '''
def perimeter(a, b):
    return a*2 + b*2

class RectangleTestCase(unittest.TestCase):

   def test_area_1(self):
       res = area(2, 3)
       self.assertAlmostEqual(res, 6, delta=0.1)
   def test_perimeter_1(self):
       res = perimeter(2, 3)
       self.assertAlmostEqual(res, 10, delta=0.1)
   def test_area_2(self):
       res = area(0, 3)
       self.assertAlmostEqual(res, 0, delta=0.1)
   def test_perimeter_2(self):
       res = perimeter(0, 3)
       self.assertAlmostEqual(res, 6, delta=0.1)
   def test_area_3(self):
       try:
           area(5, -4)
       except ValueError:
           pass
   def test_perimeter_3(self):
       try:
           perimeter(5, -4)
       except ValueError:
           pass
   def test_area_4(self):
       res = area(5.5, 2)
       self.assertAlmostEqual(res, 11, delta=0.1)
   def test_perimeter_4(self):
       res = perimeter(5.5, 2)
       self.assertAlmostEqual(res, 15, delta=0.1)
