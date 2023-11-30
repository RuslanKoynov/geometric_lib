import unittest

def area(a):
    '''
    Возвращает площадь квадрата

        Параметры:
            a (int): сторона квадрата
        Возвращаемое значение:
            сторона в квадрате
    
    '''
    if a < 0:
        raise ValueError("Negative number")
    
    return a * a

def perimeter(a):
    '''
    Возвращает периметр квадрата

        Параметры:
            a (int): сторона квадрата
        Возвращаемое значение:
            сторона, умноженная на 4
    
    '''
    return 4 * a

class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_positive_area(self):
        res = area(5)
        self.assertEqual(res, 25)

    def test_float_area(self):
        res = area(2.5)
        self.assertEqual(res, 6.25)

    def test_negative_area(self):
        self.assertRaises(ValueError, area, -5)

    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_positive_perimeter(self):
        res = perimeter(5)
        self.assertEqual(res, 20)

    def test_float_perimeter(self):
        res = perimeter(2.5)
        self.assertEqual(res, 10)

    def test_negative_perimeter(self):
        self.assertRaises(ValueError, perimeter, -5)
