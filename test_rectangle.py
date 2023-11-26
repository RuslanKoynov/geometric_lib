import unittest

from rectangle import area
from rectangle import perimeter

class TestRectangle(unittest.TestCase):
    def test_Area1(self):
        res = area(5, 5)
        self.assertEqual(res, 25)

    def test_Area2(self):
        res = area(11, 10)
        self.assertEqual(res, 110)

    def test_Area3(self):
        res = area(2, 2)
        self.assertEqual(res, 4)

    def test_Area4(self):
        res = area(5346, 5345)
        self.assertEqual(res, 28574370)

    def test_perimetr1(self):
        res = perimeter(20, 30)
        self.assertEqual(res, 100)

    def test_perimetr1(self):
        res = perimeter(5351, 534)
        self.assertEqual(res, 11770)
