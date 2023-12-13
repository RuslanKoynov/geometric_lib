import unittest

def area(a, h):
    '''
    Возвращает периметр треугольника по алгебраической формуле.
    Параметры:
        a (int): десятичное число
        h (int): десятичное число
    Возвращаемое значение:
        a * h / 2 (int): значение вычисленного периметра
    '''
    return a * h / 2

def perimeter(a, b, c):
    '''
    Возвращает периметр треугольника по алгебраической формуле.
    Параметры:
        a (int): десятичное число
        b (int): десятичное число
        c (int): десятичное число
    Возвращаемое значение:
        a + b + c (int): значение вычисленного периметра
    '''
    return a + b + c 

class TestTriangle(unittest.TestCase):
    def test_zero_mul(self):
        res = area(0, 10)
        self.assertEqual(res, 0)

    def test_small_area(self):
        res = area(5, 4)
        self.assertEqual(res, 10)

    def test_large_area(self):
        res = area(567585, 98463293)
        self.assertEqual(res, 27943144078702.5)

    def test_small_perimetr(self):
        res = perimeter(5, 3, 4)
        self.assertEqual(res, 12)

    def test_large_perimetr(self):
        res = perimeter(476435, 39565532 ,84796317)
        self.assertEqual(res, 124838284)  

    def test_string_area(self):
        res = area("10", "5")
        self.assertEqual(res, TypeError)

    def test_string_perimetr(self):
        res = perimeter("15", "76", "43")
        self.assertEqual(res, TypeError)        