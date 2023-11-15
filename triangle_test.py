import unittest
def area(a, h):
    return a * h / 2
'''
    Принимает 2 числа, которые являются стороной и высотой треугольника: a,h
    Возвращает площадь квадрата, вычисляя его по формуле: a * h *0,5
'''
def perimeter(a, b, c):
    return a + b + c
'''
    Принимает 3 чилса, которые являются сторонами треугольника: a,b,c
    Возвращает периметр треугольника, вычисляя его по формуле : a+b+c
    '''

class TriangleTestCase(unittest.TestCase):
    def test_area_two_and_four (self) :
        res = area ( 2,  4)
        self.assertEqual (res,4)
    def test_area_three_and_four (self):
        res = area ( 3,  4)
        self.assertEqual (res,  6)
    def test_perimetr_two_two_three(self):
        res = perimeter( 2,  2, 3)
        self.assertEqual (res,  7)
    def test_perimetr_one_three_five(self):
        res = perimeter(  1,  3,  5)
        self .assertEqual(res, 9)
if __name__ == '__main__':
    unittest.main()