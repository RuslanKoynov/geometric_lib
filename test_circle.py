import unittest

from circle import area
from circle import perimeter

class TestCircle(unittest.TestCase):
    def test1_area_Circle(self):
        res = area(1)
        self.assertEqual(res, 3.141592653589793)

    def test2_area_Circle(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test3_area_Circle(self):
        res = area(15)
        self.assertEqual(res, 706.8583470577034)

    def test4_area_Circle(self):
        res = area(1243)
        self.assertEqual(res, 4853914.587836256)

    def test6_area_Circle(self):
        res = area(2.23124)
        self.assertEqual(res, 15.640205201560962)

    def test1_perimetr_Circle(self):
        res = perimeter(2)
        self.assertEqual(res, 12.566370614359172)

    def test2_perimetr_Circle(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test3_perimetr_Circle(self):
        res = perimeter(1)
        self.assertEqual(res, 6.283185307179586)

    def test5_perimetr_Circle(self):
        res = perimeter(1.123)
        self.assertEqual(res, 7.056017099962675)
