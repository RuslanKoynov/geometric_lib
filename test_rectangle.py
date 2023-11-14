import unittest

from rectangle import area
from rectangle import perimeter

class TestRectangle(unittest.TestCase):
    def test1_rectangle_area(self):
        res = area(2, 10)
        self.assertEqual(res, 20)

    def test2_rectangle_area(self):
        res = area(0, 312424124123)
        self.assertEqual(res, 0)

    def test3_rectangle_area(self):
        res = area(12, 100)
        self.assertEqual(res, 1200)

    def test4_rectangle_area(self):
        res = area(5, 5)
        self.assertEqual(res, 25)

    def test5_rectangle_area(self):
        res = area(1, 1)
        self.assertEqual(res, 1)

    def test1_rectangle_perimetr(self):
        res = perimeter(12, 21)
        self.assertEqual(res, 66)

    def test2_rectangle_perimetr(self):
        res = perimeter(1234, 4321)
        self.assertEqual(res, 11110)

    def test3_rectangle_perimetr(self):
        res = perimeter(1, 1)
        self.assertEqual(res, 4)