import unittest

from square import area
from square import perimeter


class Test(unittest.TestCase):
    def test_area_1(self):
        res = area(1)
        self.assertEqual(res, 1)

    def test_area_2(self):
        res = area(25)
        self.assertEqual(res, 625)

    def test_area_3(self):
        res = area(0.4)
        self.assertEqual(res,  0.16)

    def test_area_4(self):
        res = area(7.77)
        self.assertEqual(res,  60.3729)

    def test_perimeter_1(self):
        res = perimeter(5)
        self.assertEqual(res, 20)

    def test_perimeter_2(self):
        res = perimeter(30.5)
        self.assertEqual(res, 122)

    def test_perimeter_3(self):
        res = perimeter(6.13)
        self.assertEqual(res, 24.52)

    def test_perimeter_4(self):
        res = perimeter(0.027)
        self.assertEqual(res, 0.108)

    def test_area_5(self):
        res = area(-777)
        self.assertEqual(res, "Нельзя вводить отрицательные числа!")

    def test_perimeter_5(self):
        res = perimeter(-2)
        self.assertEqual(res, "Нельзя вводить отрицательные числа!")

    def test_area_6(self):
        res = area("&")
        self.assertEqual(res, "Нельзя вводить символы!")

    def test_perimeter_6(self):
        res = perimeter("abc")
        self.assertEqual(res, "Нельзя вводить строки!")