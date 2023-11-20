import unittest

def area(a, b):
    '''Принимает десятичные числа a и b, возвращает их произведение'''
    return a * b

def perimeter(a, b):
    '''Принимает десятичные числа a и b, возвращает их сумму, умноженную на 2'''
    return (a + b)*2

class RectangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        """
        Тестирование функции area на получение в виде аргумента числа 0
        """
        res = area(0, 1)
        res1 = area(1,0)
        self.assertEqual(res, 0)
        self.assertEqual(res1, 0)

    def test_area_multiple(self):
        """
        Тестирование фукнции area на получение целочисленных значений.
        """
        res = area(5, 5)
        res1 = area(2, 100)
        res2 = area(2, 2)
        self.assertEqual(res, 25)
        self.assertEqual(res1, 200)
        self.assertEqual(res2, 4)


    def test_perimetr_zero(self):
        """
        Тестирование функции perimetr на получение аргумента 0.
        """
        res = area(0, 1)
        res1 = area(1, 0)
        self.assertEqual(res, 0)
        self.assertEqual(res1, 0)


    def test_perimetr_multiple(self):
        """
        Тестирование функции perimetr на получение целочисленных значений.
        """
        res = perimetr(10, 2)
        res1 = perimetr(4, 5)
        res2 = perimetr(1, 1)
        self.assertEqual(res, 24)
        self.assertEqual(res1, 18)
        self.assertEqual(res2, 4)