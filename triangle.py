import unittest

def area(a, h):
    '''
    Возвращает площадь треугольника

        Параметры:
            a (int): сторона треугольника, на которую опущена высота
            h (int): высота треугольника
            
        Возвращаемое значение:
            сторона, умноженная на высоту и все это деленное на 2
    
    '''
    if a <= 0 or h <= 0:
        raise ValueError("Non-positive values are not allowed")
    
    return a * h / 2 

def perimeter(a, b, c):
     '''
    Возвращает периметр треугольника

        Параметры:
            a (int): первая сторона треугольника
            b (int): вторая сторона треугольника
            c (int): третья сторона треугольника
            
        Возвращаемое значение:
            периметр треугольника (сумма длин всех его сторон)
    
    '''
     if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Non-positive values are not allowed")
    
     return a + b + c 

class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0, 5)
        self.assertEqual(res, 0)

    def test_positive_area(self):
        res = area(10, 5)
        self.assertEqual(res, 25)

    def test_float_area(self):
        res = area(7.5, 3)
        self.assertEqual(res, 11.25)

    def test_negative_area(self):
        self.assertRaises(ValueError, area, -10, 5)

    def test_zero_perimeter(self):
        res = perimeter(0, 5, 7)
        self.assertEqual(res, 12)

    def test_positive_perimeter(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_float_perimeter(self):
        res = perimeter(3.5, 6, 8)
        self.assertEqual(res, 17.5)

    def test_negative_perimeter(self):
        self.assertRaises(ValueError, perimeter, -10, 5, 7)
