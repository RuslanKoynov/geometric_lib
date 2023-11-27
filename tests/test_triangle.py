import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    def test_area_1(self):
        res = area(5, 23)
        self.assertEqual(res, 57.5)

    def test_area_2(self):
        res = area(543753278, 6576754)
        self.assertEqual(res, 1788065773049806.0)

    def test_area_3(self):
        res = area(65.7, 56.43)
        self.assertAlmostEqual(res, 1853.7255)

    def test_area_4(self):
        res = area(-98, 9)
        self.assertEqual(res, 0)

    def test_perimeter_1(self):
        res = perimeter(56, 56, 34)
        self.assertEqual(res, 146)

    def test_perimeter_2(self):
        res = perimeter(745367436, 5895789763, 578343644)
        self.assertEqual(res, 7219500843)

    def test_perimeter_3(self):
        res = perimeter(8, 76.3, 12.96)
        self.assertAlmostEqual(res, 97.26)

    def test_perimeter_4(self):
        res = perimeter(-13, 9, -5)
        self.assertEqual(res, 0)
