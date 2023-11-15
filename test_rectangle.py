import unittest

from rectangle import area
from rectangle import perimeter

class Test(unittest.TestCase):
    def test_area_1(self):
        res = area(0, 2)
        self.assertEqual(res, 0)
    def test_area_2(self):
        res = area(4, 0)
        self.assertEqual(res, 0)

    def test_area_3(self):
        res = area(0.5, 3)
        self.assertEqual(res, 1.5)

    def test_area_4(self):
        res = area(777, 64)
        self.assertEqual(res, 49728)

    def test_perimeter_1(self):
        res = perimeter(5, 2)
        self.assertEqual(res, 3.5)

    def test_perimeter_2(self):
        res = perimeter(4, 8)
        self.assertEqual(res, 6)

    def test_perimeter_3(self):
        res = perimeter(0.5, 8)
        self.assertEqual(res, 4.25)

    def test_perimeter_4(self):
        res = perimeter(777, 64)
        self.assertEqual(res, 420.5)