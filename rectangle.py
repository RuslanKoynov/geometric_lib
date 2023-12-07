import unittest

class RectangleTestCase(unittest.TestCase):
    def test_area_test_zero(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_area_test_square(self):
        res = area(7,7)
        self.assertAlmostEqual(res,49)

    def test_area_test_float_number(self):
        res = area(7.23,9.66)
        self.assertAlmostEqual(res,69.84,places=2)

    def test_perimeter_test_zero(self):
        res = perimeter(10, 0)
        self.assertAlmostEqual(res, 0)

    def test_perimeter_test_square(self):
        res = perimeter(7,7)
        self.assertAlmostEqual(res,28)

    def test_perimeter_test_float_number(self):
        res = perimeter(7.23,9.66)
        self.assertAlmostEqual(res,33.78)

    def test_area_test_negative_number(self):
        res = area(-3,2)
        self.assertEqual(res, "ERROR")

    def test_perimeter_test_negative_number(self):
        res = perimeter(-1,2)
        self.assertEqual(res, "ERROR")


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