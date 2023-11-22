from circle import perimetr, area
import unittest

class CircleTest(unittest.TestCase):

    def test_area_Circle_Five(self):
        res = area(5)
        self.assertEqual(res, 78.53981633974483)

    def test_area_Circle_Seven(self):
        res = area(7)
        self.assertEqual(res, 153.93804002589985)

    def test_area_Circle_Nine(self):
        res = area(9)
        self.assertEqual(res, 254.46900494077323)

    def test_perimeter_Circle_Five(self):
        res = area(5)
        self.assertEqual(res, 31.41592653589793)

    def test_perimeter_Circle_MinusSeven(self):
        res = area(-7)
        self.assertEqual(res, "ERROR")

    def test_perimeter_Circle_Nine(self):
        res = area(9)
        self.assertEqual(res, 56.548667764616276)
