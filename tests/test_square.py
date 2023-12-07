import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    def test_area_1(self):
        res = area(67)
        self.assertEqual(res, 4489)

    def test_area_2(self):
        res = area(67575475467)
        self.assertEqual(res, 4566444884591118868089)

    def test_area_3(self):
        res = area(65.7)
        self.assertAlmostEqual(res, 4316.49)

    def test_area_4(self):
        res = area(-98)
        self.assertEqual(res, 0)

    def test_perimeter_1(self):
        res = perimeter(56)
        self.assertEqual(res, 224)

    def test_perimeter_2(self):
        res = perimeter(89564364645)
        self.assertEqual(res, 358257458580)

    def test_perimeter_3(self):
        res = perimeter(67.3)
        self.assertAlmostEqual(res, 269.2)

    def test_perimeter_4(self):
        res = perimeter(-13)
        self.assertEqual(res, 0)
