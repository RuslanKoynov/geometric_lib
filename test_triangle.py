import unittest

from triangle import area
from triangle import perimeter


class Test(unittest.TestCase):
    def test_area_1(self):
        res = area(1, 2)
        self.assertEqual(res, 1)

    def test_area_2(self):
        res = area(4, 3)
        self.assertEqual(res, 6)

    def test_area_3(self):
        res = area(12, 0.4)
        self.assertEqual(res,  2.4)

    def test_area_4(self):
        res = area(777, 64)
        self.assertEqual(res, 24864)

    def test_perimeter_1(self):
        res = perimeter(5, 4, 3)
        self.assertEqual(res, 12)

    def test_perimeter_2(self):
        res = perimeter(3, 4, 6)
        self.assertEqual(res, 13)

    def test_perimeter_3(self):
        res = perimeter(6.5, 6.5, 5)
        self.assertEqual(res, 18)

    def test_perimeter_4(self):
        res = perimeter(777, 645, 425)
        self.assertEqual(res, 1847)

    def test_area_5(self):
        res = area(-77, 64)
        self.assertEqual(res, "Нельзя вводить отрицательные числа!")

    def test_perimeter_5(self):
        res = perimeter(-5, -2, -6)
        self.assertEqual(res, "Нельзя вводить отрицательные числа!")

    def test_area_6(self):
        res = area("&", 64)
        self.assertEqual(res, "Нельзя вводить символы!")

    def test_perimeter_6(self):
        res = perimeter(5, "abc", 5)
        self.assertEqual(res, "Нельзя вводить строки!")
