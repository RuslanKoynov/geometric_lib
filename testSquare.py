from square import perimeter, area
import unittest

class SquareTest(unittest.TestCase):

    def test_area_Square_Five(self):
        res = area(1.5)
        self.assertEqual(res, 2.25)

    def test_area_Square_Seven(self):
        res = area(7)
        self.assertEqual(res, 49)

    def test_area_Square_Nine(self):
        res = area(9)
        self.assertEqual(res, 81)

    def test_perimeter_Square_Two(self):
        res = perimeter(2)
        self.assertEqual(res, 8)

    def test_perimeter_Square_MinusSeven(self):
        res = perimeter(-7)
        self.assertEqual(res, "ERROR")

    def test_perimeter_Square_Sixth(self):
        res = perimeter(6)
        self.assertEqual(res, 24)
