import math
import unittest


def area(r):
    ''' Принимает десятичное число r, возрващает квадрат числа r, умноженный на число Пи'''
    return math.pi * r * r


def perimeter(r):
    ''' Принимает десятичное число r, возвращает число r, умноженное на 2 и на число Пи'''
    return 2 * math.pi * r



class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        """
        Тестирование функции area на получение в виде аргумента числа 0
        """
        res = area(0)
        self.assertEqual(int(res), 0)

    def test_area_multiple(self):
        """
        Тестирование фукнции area на получение целочисленных значений.
        Округление в меньшую сторону.
        Числа после запятой отбрасываются.
        """
        res1 = area(3)
        res2 = area(4)
        res3 = area(100)
        self.assertEqual(res1, 28)
        self.assertEqual(res2, 50)
        self.assertEqual(res3, 31415)

    def test_perimetr_zero(self):
        """
        Тестирование функции perimetr на получение аргумента 0.
        """
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimetr_multiple(self):
        """
        Тестирование функции perimetr на получение целочисленных значений.
        Округление в меньшую сторону.
        Числа после запятой отбрасываются.
        """
        res1 = perimeter(3)
        res2 = perimeter(4)
        res3 = perimeter(100)
        self.assertEqual(res1, 18)
        self.assertEqual(res2, 25)
        self.assertEqual(res3, 628)