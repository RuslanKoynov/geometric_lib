import unittest


def area(a):
    '''
    Принимает число a, возвращает площадь квадрата со стороной a.
    Пример вызова функции: area(5) -> 25.
    '''
    return a * a


def perimeter(a):
    '''
    Принимает число a, возвращает периметр квадрата со стороной a.
    Пример вызова функции: perimeter(7) -> 28.
    '''
    return 4 * a


class SquareTestCase(unittest.TestCase):
    def test_area_multiply_by_zer0(self):
        res = area(0)
        self.assertEqual(res, 0)


    def test_positive_area(self):
        res = area(10)
        self.assertEqual(res, 100)


    def test_negative_area(self):
        self.assertRaises(ValueError, area, -1)


    def test_float_area(self):
        res = area(6.9)
        self.assertAlmostEqual(res, 47.61, 2)


    def test_perimeter_multiply_by_zer0(self):
        res = perimeter(0)
        self.assertEqual(res, 0)


    def test_positive_perimeter(self):
        res = perimeter(4)
        self.assertEqual(res, 16)


    def test_negative_perimeter(self):
        self.assertRaises(ValueError, perimeter, -3)


    def test_float_perimeter(self):
        res = perimeter(45.67)
        self.assertAlmostEqual(res, 182.68, 2)
