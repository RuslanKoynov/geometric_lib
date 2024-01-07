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
        self.assertAlmostEqual(res, 10, delta=0.1)
    def test_perimeter_1(self):
        res = perimeter(4, 5, 6)
        self.assertAlmostEqual(res, 15, delta=0.1)
        
    def test_area_2(self):
        try:
            area(4, -5)
        except ValueError:
            pass
            
    def test_perimeter_2(self):
        try:
            perimeter(4, 5, -6)
        except ValueError:
            pass


    def test_area_3(self):
        res = area(4, 0)
        self.assertAlmostEqual(res, 0, delta=0.1)
    def test_perimeter_3(self):
        res = perimeter(4, 5, 0)
        self.assertAlmostEqual(res, 9, delta=0.1)

    def test_area_4(self):
        res = area(4, 5.5)
        self.assertAlmostEqual(res, 11, delta=0.1)
    def test_perimeter_4(self):
        res = perimeter(4, 5.5, 6)
        self.assertAlmostEqual(res, 15.5, delta=0.1)




