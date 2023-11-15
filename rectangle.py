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
    if type(a) != int and type(b) != int:
        return f"Input data must be int"
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
    if type(a) != int and type(b) != int:
        return f"Input data must be int"
    return 2*(a + b)

class RectangleTestCase (unittest.TestCase):
    def test_zero_mul_area(self):
        res = area (10, 0)
        self.assertEqual(res, 0)

    def test_rectangle_mul_area(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_zero_mul_perimeter(self):
        res = perimeter (0, 0)
        self.assertEqual(res, 0)

    def test_rectangle_mul_perimeter(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)


    def test_rectangle_str_perimeter(self):
        res = perimeter("12", "5")
        self.assertEqual(res, "Input data must be int")

    def test_rectangle_str_area(self):
        res = area("8", "4")
        self.assertEqual(res, "Input data must be int")


    def test_rectangle_area_1(self):
        res = area(2, 8)
        self.assertEqual(res, round(16, 2))

    def test_rectangle_area_2(self):
        res = area(3, 10)
        self.assertEqual(res, round(30, 2))

    def test_rectangle_area_3(self):
        res = area(1, 1)
        self.assertEqual(res, round(1, 2))

    def test_rectangle_area_4(self):
        res = area(8, 3)
        self.assertEqual(res, round(24, 2))


    def test_rectangle_perimeter_1(self):
        res = perimeter(0, 8)
        self.assertEqual(res, round(2*(0+8), 2))

    def test_rectangle_perimeter_2(self):
        res = perimeter(56, 7)
        self.assertEqual(res, round(2* (56+7), 2))

    def test_rectangle_perimeter_3(self):
        res = perimeter(1, 5)
        self.assertEqual(res, round(2 * (1+5), 2))

    def test_rectangle_perimeter_4(self):
        res = perimeter(8, 32)
        self.assertEqual(res, round(2 * (8 + 32), 2))
