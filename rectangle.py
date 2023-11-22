import unittest

class RectangleTestCase(unittest.TestCase):
    def area_test_zero(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def area_test_square(self):
        res = area(7,7)
        self.assertEqual(res,49)

    def area_test_float_number(self):
        res = area(7.23,9.66)
        self.assertEqual(res,69.8418)

    def perimeter_test_zero(self):
        res = perimeter(10, 0)
        self.assertEqual(res, 0)

    def perimeter_test_square(self):
        res = perimeter(7,7)
        self.assertEqual(res,28)

    def perimeter_test_float_number(self):
        res = perimeter(7.23,9.66)
        self.assertEqual(res,33.78)


def area(a,b):
    """
    Возвращает площадь прямоугольника

        Параметры:
            a (int): одна из сторон прямоугольника
            b (int): вторая сторона прямоугольника

        Возвращаемое значение:
            a*b (int): произведение двух сторон
    """
    return a*b

def perimeter(a,b):
    """
    Возвращает периметр прямоугольника

        Параметры:
            a (int): одна из сторон прямоугольника
            b (int): вторая сторона прямоугольника

        Возвращаемое значение:
            (a + b)*2 (int): удвоенная сумма сторон
    """
    return (a + b)*2

print(perimeter(-7,8))