import unittest

from circle import area
from circle import perimeter


class Test(unittest.TestCase):
    def test_area_1(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_2(self):
        res = area(6)
        self.assertEqual(res, 113.09733552923255)

    def test_area_3(self):
        res = area(0.5)
        self.assertEqual(res, 0.7853981633974483)

    def test_area_4(self):
        res = area(6.5)
        self.assertEqual(res, 132.73228961416876)

    def test_perimeter_1(self):
        res = perimeter(20)
        self.assertEqual(res, 125.66370614359172)

    def test_perimeter_2(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_3(self):
        res = perimeter(0.5)
        self.assertEqual(res, 3.141592653589793)

    def test_perimeter_4(self):
        res = perimeter(1)
        self.assertEqual(res, 6.283185307179586)

    def test_area_5(self):
        res = area(-7)
        self.assertEqual(res, "Нельзя вводить отрицательные числа!")

    def test_perimeter_5(self):
        res = perimeter(-5)
        self.assertEqual(res, "Нельзя вводить отрицательные числа!")

    def test_area_6(self):
        res = area("^")
        self.assertEqual(res, "Нельзя вводить символы!")

    def test_perimeter_6(self):
        res = perimeter("abc")
        self.assertEqual(res, "Нельзя вводить строки!")