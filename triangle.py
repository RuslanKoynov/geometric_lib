import unittest

''' Принимает числа a, h и возвращает площадь треугольника '''
def area(a, h):
    return a * h / 2
''' Принимает числа a, b, c и возвращает периметр треугольника '''
def perimeter(a, b, c): 
    return a + b + c 

class TriangleTestCase(unittest.TestCase):
   def test_area_1(self):
       res = area(4, 5)
       self.assertEqual(res, 10)
   def test_perimeter_1(self):
       res = perimeter(4, 5, 6)
       self.assertEqual(res, 15)

   def test_area_2(self):
       res = area(4, -5)
       self.assertEqual(res, "a or b can not be negative")
   def test_perimeter_2(self):
       res = perimeter(4, 5, -6)
       self.assertEqual(res, "a or b can not be negative")

   def test_area_1(self):
       res = area(4, 0)
       self.assertEqual(res, 0)
   def test_perimeter_1(self):
       res = perimeter(4, 5, 0)
       self.assertEqual(res, 9)

   def test_area_4(self):
       res = area(4, 5.5)
       self.assertEqual(res, 11)
   def test_perimeter_4(self):
       res = perimeter(4, 5.5, 6)
       self.assertEqual(res, 15.5)




