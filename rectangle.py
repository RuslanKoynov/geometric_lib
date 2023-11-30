import unittest

def area(a, b):
    '''
    Возвращает площадь прямоугольника

        Параметры:
            a (int): сторона прямоугольника
            b (int): сторона прямоугольника
        Возвращаемое значение:
            a * b (площадь прямоугольника)
    '''
    if a < 0 or b < 0:
        raise ValueError("Negative number")

    return a * b

def perimeter(a, b):
    '''
    Возвращает периметр прямоугольника

        Параметры:
            a (int): сторона прямоугольника
            b (int): сторона прямоугольника
        Возвращаемое значение:
            удвоенная сумма a и b (периметр прямоугольника)
    '''
    return (a + b) * 2

class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0, 5)
        self.assertEqual(res, 0)

    def test_positive_area(self):
        res = area(10, 5)
        self.assertEqual(res, 50)

    def test_float_area(self):
        res = area(7.5, 3)
        self.assertEqual(res, 22.5)

    def test_negative_area(self):
        self.assertRaises(ValueError, area, -10, 5)

    def test_zero_perimeter(self):
        res = perimeter(0, 5)
        self.assertEqual(res, 10)

    def test_positive_perimeter(self):
        res = perimeter(10, 5)
        self.assertEqual(res, 30)

    def test_float_perimeter(self):
        res = perimeter(7.5, 3)
        self.assertEqual(res, 21)

    def test_negative_perimeter(self):
        self.assertRaises(ValueError, perimeter, -10, 5)
