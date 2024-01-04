import unittest


def area(a, b):
    '''
    Принимает числа a и b, возвращает площадь прямоугольника со сторонами длиной a и b.
    Пример вызова функции: area(4, 9) -> 36.
    '''
    return a * b


def perimeter(a, b):
    '''
    Принимает числа a и b, возвращает периметр прямоугольника со сторонами длиной a и b.
    Пример вызова функции: perimeter(6, 7) -> 30.
    '''
    return 2 * (a + b)


class RectangleTestCase(unittest.TestCase):
    def test_area_multiply_by_zer0(self):
        res = area(10, 0)
        self.assertEqual(res, 0)


    def test_positive_area(self):
        res = area(15, 10)
        self.assertEqual(res, 150)


    def test_negative_area(self):
        self.assertRaises(ValueError, area, -1, 2)
        self.assertRaises(ValueError, area, 1, -2)
        self.assertRaises(ValueError, area, -1, -2)


    def test_float_area(self):
        res = area(3.7, 8.4)
        self.assertAlmostEqual(res, 31.08, 2)


    def test_perimeter_multiply_by_zer0(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)


    def test_positive_perimeter(self):
        res = perimeter(1, 1)
        self.assertEqual(res, 4)


    def test_negative_perimeter(self):
        self.assertRaises(ValueError, perimeter, -3, 3)
        self.assertRaises(ValueError, perimeter, 3, -3)
        self.assertRaises(ValueError, perimeter, -3, -3)


    def test_float_perimeter(self):
        res = perimeter(3.37, 2.56)
        self.assertAlmostEqual(res, 11.86, 2)
    