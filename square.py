import unittest

def area(a):
    '''
    Возвращает площадь квадрата.

        Параметры:
            a(int): сторона квадрата
        
        Возвращенное значение:
            a * a (int): площадь квадрата 
    '''
    return a * a


def perimeter(a):
    '''
    Возвращает периметр квадрата.

        Параметры:
            a(int): сторона квадрата
        
        Возвращенное значение:
            4 * a (int): периметр квадрата 
    '''
    return 4 * a


class SquareTestCase(unittest.TestCase):
    def test_area_1(self):
        res = area(7)
        self.assertEqual(res, 49)
       
    def test_area_2(self):
        res = area(18.2)
        self.assertAlmostEqual(res, 331.24)

    def test_area_3(self):
        with self.assertRaises(Exception):
            area(-5789325)

    def test_perimeter_1(self):
        res = perimeter(7)
        self.assertEqual(res, 28)
    
    def test_perimeter_2(self):
        res = perimeter(18.2)
        self.assertAlmostEqual(res, 72.8)
    
    def test_perimeter_3(self):
        rwith self.assertRaises(Exception):
            perimeter(-5789325)