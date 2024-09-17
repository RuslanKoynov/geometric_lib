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
    if type(a) != int and type(h) != int:
        return f"Input data must be int"
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
    if type(a) != int and type(b) != int and type(c) != int:
        return f"Input data must be int"
    return a + b + c

class TriangleTestCase (unittest.TestCase):
    def test_zero_mul_area(self):
        res = area (10, 0)
        self.assertEqual(res, 0)

    def test_triangle_mul_area(self):
        res = area(10, 10)
        self.assertEqual(res, 50)

    def test_zero_mul_perimeter(self):
        res = perimeter (0, 0, 0)
        self.assertEqual(res, 0)

    def test_triangle_mul_perimeter(self):
        res = perimeter(10, 10, 10)
        self.assertEqual(res, 30)


    def test_triangle_str_perimeter(self):
        res = perimeter("12", "8", "3")
        self.assertEqual(res, "Input data must be int")

    def test_triangle_str_area(self):
        res = area("8", "65")
        self.assertEqual(res, "Input data must be int")

    def test_triangle_area_1(self):
        res = area(2, 9)
        self.assertEqual(res, round(2*9/2, 2))

    def test_triangle_area_2(self):
        res = area(0, 6)
        self.assertEqual(res, round(0*6/2, 2))

    def test_triangle_area_3(self):
        res = area(6, 8)
        self.assertEqual(res, round(6*8/2, 2))

    def test_triangle_area_4(self):
        res = area(3, 88)
        self.assertEqual(res, round(3*88/2, 2))


    def test_triangle_perimeter_1(self):
        res = perimeter(90, 3, 7)
        self.assertEqual(res, round(90 + 3 + 7, 2))

    def test_triangle_perimeter_2(self):
        res = perimeter(43, 71, 4)
        self.assertEqual(res, round(43 + 71 + 4, 2))

    def test_triangle_perimeter_3(self):
        res = perimeter(3, 0, 85)
        self.assertEqual(res, round(3 + 0 + 85, 2))

    def test_triangle_perimeter_4(self):
        res = perimeter(32, 5, 4)
        self.assertEqual(res, round(32 + 5 + 4, 2))
