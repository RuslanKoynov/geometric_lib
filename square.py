import unittest, random
def area(a):
    '''
    Вычисление площади квадрата
    Параметр:
        a(int/float) - сторона квадрата
    Возвращаемое значение:
        a * a(int/float) - площадь квадрата
    Пример вызова:
        area(10) = 100
    '''
    return a * a


def perimeter(a):
    '''
    Вычисление периметра квадрата
    Параметры:
        a(int/float) - сторона квадрата
    Возвращаемое значение:
        4 * a(int/float) - площадь квадрата
    Пример вызова:
        perimeter(10) = 40
    '''
    return 4 * a

class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)
    def test_small_numbers_area(self):
        res = area(15)
        self.assertEqual(res, 15**2)