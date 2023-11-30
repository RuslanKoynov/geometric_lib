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

    def test_area_positive_values(self):
        res = area(5, 10)
        self.assertEqual(res, 25)

    def test_area_negative_values(self):
        with self.assertRaises(ValueError):
            area(-3, 8)

    def test_perimeter_zero_values(self):
        with self.assertRaises(ValueError):
            perimeter(0, 0, 0)

    def test_perimeter_mixed_values(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_area_float_values(self):
        res = area(2.5, 4)
        self.assertAlmostEqual(res, 5, places=2)

    def test_perimeter_float_values(self):
        res = perimeter(3.5, 6, 8)
        self.assertAlmostEqual(res, 17.5, places=2) 

if __name__ == '__main__':
    unittest.main()
