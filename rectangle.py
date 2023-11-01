import unittest

class RectangleTestCase(unittest.TestCase):
    
    def test_zero_mul(self):
       res = area(10, 0)
       self.assertEqual(res, 0)
       
    def test_square_mul(self):
       res = area(10, 10)
       self.assertEqual(res, 100)
       
    def test_perimeter(self):
       res = perimeter(10, 5)
       self.assertEqual(res, 30)
       
def area (a,b):
    ''' Принимает на вход числа a и b, возвращает площадь прямоугольника '''
    return a * b

def perimeter(a,b):
    ''' Принимает на вход числа a и b, возвращает периметр прямоугольника '''
    return (a + b) * 2
