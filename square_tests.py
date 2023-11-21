from square import area, perimeter
import unittest

class SquareTestCase(unittest.TestCase):
    def test_square_area(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_square_area_2(self):
        res = area(13)
        self.assertEqual(res, 169)

    def test_square_area_3(self):
        res = area(1)
        self.assertEqual(res, 1)

    def test_square_area_negative(self):
        res = area(-8)
        self.assertEqual(res, "ERROR")

    def test_square_perimeter(self):
        res = perimeter(10)
        self.assertEqual(res, 40)

    def test_square_perimeter_2(self):
        res = perimeter(51)
        self.assertEqual(res, 204)

    def test_square_perimeter_3(self):
        res = perimeter(3)
        self.assertEqual(res, 12)

    def test_square_perimeter_negative(self):
        res = perimeter(-99)
        self.assertEqual(res, "ERROR")
