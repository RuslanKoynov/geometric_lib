from circle import perimeter, area
import unittest

class CircleTest(unittest.TestCase):

    def test_area_Circle_Five(self):
        res = area(1.3)
        self.assertAlmostEqual(res, 5.31,places=2)

    def test_area_Circle_Seven(self):
        res = area(7)
        self.assertAlmostEqual(res, 153.94, places=2)

    def test_area_Circle_Nine(self):
        res = area(9)
        self.assertAlmostEqual(res, 254.47, places=2)

    def test_perimeter_Circle_Five(self):
        res = perimeter(5)
        self.assertAlmostEqual(res, 31.42, places=2)

    def test_perimeter_Circle_MinusSeven(self, places=2):
        res = perimeter(-7)
        self.assertEqual(res, "ERROR")

    def test_perimeter_Circle_Nine(self):
        res = perimeter(9)
        self.assertAlmostEqual(res, 56.55, places=2)
