import unittest


def area(a, h):
    '''
    Принимает числа a и h, возвращает площадь треугольника
    со основанием длиной a и высотой длиной h.
    Пример вызова функции: area(22, 8) -> 88.0.
    '''
    return a * h / 2


def perimeter(a, b, c):
    '''
    Принимает числа a, b и c, возвращает периметр треугольника
    со сторонами длиной a, b и c.
    Пример вызова функции: perimeter(3, 4, 5) -> 12.
    '''
    return a + b + c


class TriangleTestCase(unittest.TestCase):
    def test_area_multiply_by_zer0(self):
        res = area(10, 0)
        self.assertEqual(res, 0)


    def test_positive_area(self):
        res = area(51, 61)
        self.assertAlmostEqual(res, 1555.5, 1)


    def test_negative_area(self):
        self.assertRaises(ValueError, area, -1, 2)
        self.assertRaises(ValueError, area, 1, -2)
        self.assertRaises(ValueError, area, -1, -2)


    def test_float_area(self):
        res = area(2.8, 3.9)
        self.assertAlmostEqual(res, 5.46, 2)


    def test_perimeter_zer0(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)


    def test_positive_perimeter(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)


    def test_negative_perimeter(self):
        self.assertRaises(ValueError, perimeter, -3, 3, 3)
        self.assertRaises(ValueError, perimeter, 3, -3, 3)
        self.assertRaises(ValueError, perimeter, 3, 3, -3)
        self.assertRaises(ValueError, perimeter, -3, -3, 3)
        self.assertRaises(ValueError, perimeter, 3, -3, -3)
        self.assertRaises(ValueError, perimeter, -3, 3, -3)
        self.assertRaises(ValueError, perimeter, -3, -3, -3)


    def test_float_perimeter(self):
        res = perimeter(5.6, 8.7, 1.23)
        self.assertAlmostEqual(res, 15.53, 2)
