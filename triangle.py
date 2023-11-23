import unittest

def area(a, h):
    '''
    Возвращает площадь треугольника.

        Параметры:
            a(int): сторона треугольника
            b(int): высота треугольника 
        
        Возвращенное значение:
            a * h / 2 (int): площадь треугольника 
    '''
    return a * h / 2

def perimeter(a, b, c):
    '''
    Возвращает периметр треугольника.

        Параметры:
            a(int): сторона a треугольника
            b(int): сторона b треугольника 
            c(int): сторона c треугольника
        
        Возвращенное значение:
            a + b + c (int): периметр треугольника 
    '''
    return a + b + c


class SquareTestCase(unittest.TestCase):
    def test_area_1(self):
        res = area(4, 7)
        self.assertEqual(res, 14.0)
       
    def test_area_2(self):
        res = area(67.3, 12.5)
        self.assertAlmostEqual(res, 420.625)

    def test_area_3(self):
        res = area(327565, -87742)
        self.assertEqual(res, 14370604115.0)

    def test_perimeter_1(self):
        res = perimeter(3, 7, 9)
        self.assertEqual(res, 19)
    
    def test_perimeter_2(self):
        res = perimeter(8, 76.3, 12.96)
        self.assertAlmostEqual(res, 97.26)
    
    '''def test_perimeter_3(self):
        res = perimeter(245656, 8769583, -13)
        self.assertEqual(res, 9015252)'''