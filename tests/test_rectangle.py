import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):

    def test_area_1(self):
        res = area(5, 2)
        self.assertEqual(res, 10)

    def test_area_2(self):
        res = area(12.3, 78.4)
        self.assertAlmostEqual(res, 964.32)

    def test_area_3(self):
        res = area(67634565436345857, 5846453643634379)
        self.assertEqual(res, 395422351530952068252550699417803)

    def test_area_4(self):
        res = area(-10, 56)
        self.assertEqual(res, 0)

    def test_perimeter_1(self):
        res = perimeter(5, 2)
        self.assertEqual(res, 14)

    def test_perimeter_2(self):
        res = perimeter(54325235534, 5832489528953)
        self.assertEqual(res, 11773629528974)

    def test_perimeter_3(self):
        res = perimeter(12.3, 78.4)
        self.assertAlmostEqual(res, 181.4)

    def test_perimeter_4(self):
        res = perimeter(-5, 8)
        self.assertEqual(res, 0)

