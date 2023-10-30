import unittest
def area(a, h):
    '''
    Возвращает площадь треугольника по заданным основанию и высоте.

        Параметры:
            a (int): основание треугольника
            h (int): высота треугольника

        Возвращаемые значения:
            area (int): площадь треугольника
    '''
    return a * h / 2

def perimeter(a, b, c):
    '''
    Возвращает периметр треугольника по заданным сторонам.

        Параметры:
            a (int): первая сторона треугольника
            b (int): вторая сторона треугольника
            c (int): третья сторона треугольника

        Возвращаемые значения:
            perimetr (int): периметр прямоугольника
    '''
    return a + b + c

class TriangleTestCase (unittest.TestCase):
    def test_zero_mul_area(self):
        res = area (10, 0)
        self.assertEqual(res, 0)

    def test_square_mul_area(self):
        res = area(10, 10)
        self.assertEqual(res, 50)

    def test_zero_mul_perimeter(self):
        res = perimeter (0, 0, 0)
        self.assertEqual(res, 0)

    def test_square_mul_perimeter(self):
        res = perimeter(10, 10, 10)
        self.assertEqual(res, 30)
