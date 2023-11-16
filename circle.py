import math
import unittest


def area(r):
    return math.pi * r * r


def perimeter(r):
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
        Тестирование фукнции area на получиени целочисленных различных значений
        Округление происходит в меньшую сторону, числа после запятой отбрасываются
        """
        res1 = area(10)
        res2 = area(12)
        res3 = area(4)
        self.assertEqual(int(res1), 314)
        self.assertEqual(int(res2), 452)
        self.assertEqual(int(res3), 50)


    def test_perimetr_zero(self):
        """
        Тестирование функции perimetr на получение в виде аргумента числа 0
        """
        res = perimeter(0)
        self.assertEqual(int(res), 0)
    
    def test_perimetr_multiple(self):
        """
        Тестирование функции perimetr на получение целочисленных различных значений
        Округление происходит в меньшую сторону, числа после запятой отбрасываются
        """
        res1 = perimeter(10)
        res2 = perimeter(12)
        res3 = perimeter(4)
        self.assertEqual(int(res1), 62)
        self.assertEqual(int(res2), 75)
        self.assertEqual(int(res3), 25)