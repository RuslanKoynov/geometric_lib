import unittest
class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
       res = area(10, 0)
       self.assertEqual(res, 0)
       
    def test_square_mul(self):
       res = area(10, 10)
       self.assertEqual(res, 50)

    def test_perimetr(self):
       res = perimetr(10,5,100)
       self.assertEqual(res, 115)
       
def area(a,h):
    ''' Принимает высоту треугольника - h, и основание - a: возвращает площадь треугольника '''
    return a * h / 2

def perimetr(a,b,c):
    ''' Принимает три стороны треугольника - a,b,c: возвращает периметр треугольника'''
    return a + b + c

