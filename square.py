import unittest

def area(a):
    '''
    Возвращает квадрат числа а - площадь квадрата.
    Параметры:
        a (int): десятичное число
    Возвращаемое значение:
        a*a (int): квадрат числа а
    '''
    return a * a


def perimeter(a):
    '''
    Возвращает число а умноженное на 4 - периметр квадрата.
    Параметры:
        a (int): десятичное число
    Возвращаемое значение:
        4*a (int): десятичное число а умноженное на 4
    '''
    return 4 * a

class TestCircle(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_small_area(self):
        res = area(1)
        self.assertEqual(res, 1)

    def test_large_area(self):
        res = area(123456)
        self.assertEqual(res, 15241383936)

    def test_small_perimetr(self):
        res = perimeter(25)
        self.assertEqual(res, 100)

    def test_large_perimetr(self):
        res = perimeter(987654321)
        self.assertEqual(res, 3950617284)

    def test_string_area(self):
        res = area("10")
        self.assertEqual(res, TypeError)

    def test_string_perimetr(self):
        res = perimeter("1")
        self.assertEqual(res, TypeError)  