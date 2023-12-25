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
       self.assertAlmostEqual(res, 16, delta=0.1)
   def test_perimeter_1(self):
       res = perimeter(4)
       self.assertAlmostEqual(res, 16, delta=0.1)

   def test_area_2(self):
       with self.assertRaises(ValueError):
           area(-4)
   def test_perimeter_2(self):
       with self.assertRaises(ValueError):
           perimeter(-4)

   def test_area_3(self):
       res = area(0)
       self.assertAlmostEqual(res, 0, delta=0.1)
   def test_perimeter_3(self):
       res = perimeter(0)
       self.assertAlmostEqual(res, 0, delta=0.1)

   def test_area_4(self):
       res = area(4.5)
       self.assertAlmostEqual(res, 20.25, delta=0.1)
   def test_perimeter_4(self):
       res = perimeter(4.5)
       self.assertAlmostEqual(res, 18, delta=0.1)
