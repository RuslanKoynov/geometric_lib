import unittest
import math


def area(r):
    '''
    Возвращает площадь круга.
    Параметры:
        r (int): десятичное число
    Возвращаемое значение:
        math.pi * r * r (int): площадь круга
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает периметр.
    Параметры:
        r (int): десятичное число
    Возвращаемое значение:
        2 * math.pi * r (int): периметр
    '''
    return 2 * math.pi * r

class TestCircle(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_small_area(self):
        res = area(1)
        self.assertEqual(res, 3.141592653589793)

    def test_large_area(self):
        res = area(123456789)
        self.assertEqual(res, 47882831830708840) 

    def test_small_perimetr(self):
        res = perimeter(20)
        self.assertEqual(res, 125.66370614359172)

    def test_large_perimetr(self):
        res = perimeter(75384901072)
        self.assertEqual(res, 473657302798.77704)   

    def test_string_area(self):
        res = area("10")
        self.assertEqual(res, TypeError)

    def test_string_perimetr(self):
        res = perimeter("1")
        self.assertEqual(res, TypeError)        