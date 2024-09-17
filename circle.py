import unittest
from math import pi

def area(r):
    '''
        Возвращает площадь круга по заданным сторонам.

            Параметры:
                r (int): радиус круга

            Возвращаемые значения:
                area (int): площадь круга
        '''
    if type(r) != int:
        return f"Input data must be int"
    return round(r * r * pi, 2)


def perimeter(r):
    '''
        Возвращает периметр круга по заданным сторонам.

            Параметры:
                r (int): радиус круга

            Возвращаемые значения:
                perimetr (int): периметр круга
        '''
    if type(r) != int:
        return f"Input data must be int"
    return round(2 * pi * r, 2)

class CircleTestCase (unittest.TestCase):
    def test_zero_mul_area(self):
        res = area (0)
        self.assertEqual(res, 0)

    def test_circle_mul_area(self):
        res = area(10)
        self.assertEqual(res, round(100 * pi, 2))

    def test_zero_mul_perimeter(self):
        res = perimeter (0)
        self.assertEqual(res, 0)

    def test_circle_mul_perimeter(self):
        res = perimeter(10)
        self.assertEqual(res, round(20 * pi, 2))

    def test_circle_str_perimeter(self):
        res = perimeter("12")
        self.assertEqual(res, "Input data must be int")

    def test_circle_str_area(self):
        res = area("8")
        self.assertEqual(res, "Input data must be int")


    def test_circle_area_1(self):
        res = area(2)
        self.assertEqual(res, round(4 * pi, 2))

    def test_circle_area_2(self):
        res = area(30)
        self.assertEqual(res, round(900 * pi, 2))

    def test_circle_area_3(self):
        res = area(1)
        self.assertEqual(res, round(1 * pi, 2))

    def test_circle_area_4(self):
        res = area(9)
        self.assertEqual(res, round(81 * pi, 2))


    def test_circle_perimeter_1(self):
        res = perimeter(3)
        self.assertEqual(res, round(6 * pi, 2))

    def test_circle_perimeter_2(self):
        res = perimeter(8)
        self.assertEqual(res, round(16 * pi, 2))

    def test_circle_perimeter_3(self):
        res = perimeter(17)
        self.assertEqual(res, round(34 * pi, 2))

    def test_circle_perimeter_4(self):
        res = perimeter(30)
        self.assertEqual(res, round(60 * pi, 2))


