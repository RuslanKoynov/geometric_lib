import unittest
import math

'''Принимает число r и возвращает площадь круга'''

def area(r):
    return math.pi * r * r

'''Пример вызова:
    result = area(5)
    print(result) # Выведет 78.5'''
    
'''Приннимает число r и возвращает периметр круга'''

def perimeter(r):
    return 2 * math.pi * r

'''Пример вызова:
    result = perimeter(5)
    print(result) # Выведет 31.4'''

class CircleTestCase(unittest.TestCase):
   def test_area_1(self):
       res = area(0)
       self.assertEqual(res, 0)
       
   def test_perimeter_1(self):
       res = perimeter(0)
       self.assertEqual(res, 0)

   def test_area_2(self):
       res = area(5)
       self.assertEqual(res, 78.5)
       
   def test_perimeter_2(self):
       res = perimeter(5)
       self.assertEqual(res, 31.4)

   def test_area_3(self):
       res = area(-5)
       self.assertEqual(res, "error: radius can not be negative")
       
   def test_perimeter_3(self):
       res = perimeter(-5)
       self.assertEqual(res, "error: radius can not be negative")




    
    
