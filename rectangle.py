import unittest


def area(a, b):
    '''
    Возвращает площадь прямоугольника по заданным сторонам.

        Параметры:
            a (int): длина прямоугольника
            b (int): ширина прямоугольника

        Возвращаемые значения:
            area (int): площадь прямоугольника
    '''
    return a * b

def perimeter(a, b):
    '''
    Возвращает периметр прямоугольника по заданным сторонам.

        Параметры:
            a (int): длина прямоугольника
            b (int): ширина прямоугольника

        Возвращаемые значения:
            perimetr (int): периметр прямоугольника
    '''
    return 2*(a + b)

class RectangleTestCase (unittest.TestCase):
    def test_zero_mul_area(self):
        res = area (10, 0)
        self.assertEqual(res, 0)

    def test_square_mul_area(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_zero_mul_perimeter(self):
        res = perimeter (0, 0)
        self.assertEqual(res, 0)

    def test_square_mul_perimeter(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)
