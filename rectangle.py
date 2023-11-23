import unittest

def area(a, b):
    '''
    Возвращает площадь прямоугольника.

        Параметры:
            a(int): сторона a прямоугольника
            b(int): сторона b прямоугольника
        
        Возвращенное значение:
            a * b (int): площадь прямоугольника 
    '''
    return a * b

def perimeter(a, b):
    '''
    Возвращает периметр прямоугольника.

        Параметры:
            a(int): сторона a прямоугольника
            b(int): сторона b прямоугольника 
        
        Возвращенное значение:
            (a + b) * 2 (int): периметр прямоугольника 
    '''
    return (a + b)*2


class RectangleTestCase(unittest.TestCase):
    def test_area_1(self):
        res = area(5, 10)
        self.assertEqual(res, 50)
       
    def test_area_2(self):
        res = area(12.3, 78.4)
        self.assertAlmostEqual(res, 964.32)

    def test_area_3(self):
        res = area(987325, -123589)
        self.assertEqual(res, 122022509425)

    def test_perimeter_1(self):
        res = perimeter(5, 10)
        self.assertEqual(res, 30)
    
    def test_perimeter_2(self):
        res = perimeter(12.3, 78.4)
        self.assertAlmostEqual(res, 181.4)
    
    def test_perimeter_3(self):
        res = perimeter(987325, -123589)
        self.assertEqual(res, 2221828)