import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    def test_square_area_positive(self):
        res = area(5)
        self.assertEqual(res, 25)

    def test_square_area_negative(self):
        res = area(-5)
        self.assertRaises(res, Exception)

    def test_square_area_real(self):
        res = area(6.5)
        self.assertEqual(res, 42.25)

    def test_square_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_square_perimeter_positive(self):
        res = perimeter(6)
        self.assertEqual(res, 24)

    def test_square_perimeter_negative(self):
        res = perimeter(-6)
        self.assertRaises(res, Exception)

    def test_square_perimeter_real(self):
        res = perimeter(6.5)
        self.assertEqual(res, 26)

    def test_square_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
if __name__ == '__main__':
    unittest.main()
