import unittest
def area(a, b):
    '''
    Принимает числа, которые являются сторонами прямоугольника
    Возвращает площадь прямоугольника, вычисляя ее по формуле: S=ab
    '''
    return a * b
def perimeter(a, b):
    '''
    Принимает числа, которые являются сторонами прямоугольника
    Возвращает периметр прямоугольника, вычисляя ее по формуле: P=2a+2b
    '''
    return 2*a + 2*b
class RectangleTestCase(unittest.TestCase):
   def test_zero_mul(self):
       res = area(10, 0)
       self.assertEqual(res, 0)
       
   def test_square_mul(self):
       res = area(10, 10)
       self.assertEqual(res, 100)


