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
        self.assertEqual(res, 0)

    def test_area_multiple(self):
        """
        Тестирование фукнции area на получиени целочисленных различных значений
        Округление происходит в меньшую сторону, числа после запятой отбрасываются
        """
        res1 = area(10)
        res2 = area(12)
        self.assertAlmostEqual(res1, 314.16, places=2)
        self.assertAlmostEqual(res2, 452.39, places=2)

    def test_area_float_number(self):
        res = area(4.12)
        self.assertAlmostEqual(res, 53.33, places=2)

    def test_area_negative_number(self):
        with self.assertRaises(Exception):
            area(-10)


    def test_perimetr_zero(self):
        """
        Тестирование функции perimetr на получение в виде аргумента числа 0
        """
        res = perimeter(0)
        self.assertEqual(res, 0)
    
    def test_perimetr_multiple(self):
        """
        Тестирование функции perimetr на получение целочисленных различных значений
        Округление происходит в меньшую сторону, числа после запятой отбрасываются
        """
        res1 = perimeter(10)
        res2 = perimeter(12)
        self.assertAlmostEqual(res1, 62.83, places=2)
        self.assertAlmostEqual(res2, 75.4, places=1)

    def test_perimetr_negative_number(self):
        with self.assertRaises(Exception):
            perimeter(-10)

    def test_perimetr_float_number(self):
        res = perimeter(4.20)
        self.assertAlmostEqual(res, 26.39, places=2)
        