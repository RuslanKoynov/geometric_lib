import unittest

def area(a, b):
    '''
    Возвращает площадь прямоугольника по алгебраической формуле.
    Параметры:
        a (int): десятичное число
        b (int): десятичное число
    Возвращаемое значение:
        a * b (int): значение вычисленной площади
    '''
    return a * b

def perimeter(a, b):
    '''
    Возвращает периметр прямоугольника по алгебраической формуле.
    Параметры:
        a (int): десятичное число
        b (int): десятичное число
    Возвращаемое значение:
        (a + b)*2 (int): периметр прямоугольника
        '''
    return (a + b)*2

class TestRectangle(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_small_area(self):
        res = area(1, 1)
        self.assertEqual(res, 1)

    def test_large_area(self):
        res = area(1234, 4321)
        self.assertEqual(res, 5332114)

    def test_small_perimetr(self):
        res = perimeter(30, 15)
        self.assertEqual(res, 90)

    def test_large_perimetr(self):
        res = perimeter(346786, 345267)
        self.assertEqual(res, 1384106)

    def test_string_area(self):
        res = area("10", "1")
        self.assertEqual(res, TypeError)

    def test_string_perimetr(self):
        res = perimeter("1", "10")
        self.assertEqual(res, TypeError)