import math
import unittest

from circle import area
from circle import perimeter


class TestCircle(unittest.TestCase):
    def test_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area2(self):
        res = area(1)
        self.assertEqual(res, 3.141592653589793)

    def test_area3(self):
        res = area(3525)
        self.assertEqual(res, 39036252.21626168)

    def test_perimetr1(self):
        res = perimeter(30)
        self.assertEqual(res, 188.49555921538757)

    def test_perimetr2(self):
        res = perimeter(534255)
        self.assertEqual(res, 3356823.16628723)
