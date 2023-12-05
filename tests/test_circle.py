import unittest
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    def test_area_1(self):
        res = area(34)
        self.assertEqual(res, 3631.6811075498013)

    def test_area_2(self):
        res = area(91600)
        self.assertAlmostEqual(res, 26359721655.504375)

    def test_area_3(self):
        res = area(3.56)
        self.assertAlmostEqual(res, 39.81528865453561)

    def test_area_4(self):
        res = area(-100)
        self.assertEqual(res, 0)

    def test_perimeter_1(self):
        res = perimeter(56)
        self.assertEqual(res, 351.85837720205683)

    def test_perimeter_2(self):
        res = perimeter(6543634554)
        self.assertEqual(res, 41114868485.245445)

    def test_perimeter_3(self):
        res = perimeter(5.6)
        self.assertAlmostEqual(res, 35.18583772020568)

    def test_perimeter_4(self):
        res = perimeter(-13)
        self.assertEqual(res, 0)
