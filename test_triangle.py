import unittest

from triangle import area
from triangle import perimeter

class TestTriangle(unittest.TestCase):
    def test1_Triangle_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test2_Triangle_area(self):
        res = area(10, 1)
        self.assertEqual(res, 5)

    def test3_Triangle_area(self):
        res = area(15, 4);
        self.assertEqual(res, 30)

    def test4_Triangle_area(self):
        res = area(12345, 68);
        self.assertEqual(res, 419730)

    def test6_Triangle_area(self):
        res = area(12345.12314, 68.123412);
        self.assertEqual(res, 420495.9549284768)

    def test1_Triangle_perimeter(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test2_Triangle_perimeter(self):
        res = perimeter(11, 12, 13)
        self.assertEqual(res, 36)

    def test5_Triangle_perimeter(self):
        res = perimeter(11.12312412, 12.123124, 13.124123)
        self.assertEqual(res, 36.37037112)
