import unittest
from square import area, perimeter


class SquareTestCase(unittest.TestCase):
    def test_area_positive(self):
        res = area(3)
        self.assertEqual(res, 9)

    def test_area_negative(self):
        res = area(-3)
        self.assertEqual(res, "Error")

    def test_area_real(self):
        res = area(3.3)
        self.assertEqual(res, 10.889999999999999)

    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_perimeter_positive(self):
        res = perimeter(3)
        self.assertEqual(res, 12)

    def test_perimeter_negative(self):
        res = perimeter(-3)
        self.assertEqual(res, "Error")

    def test_perimeter_real(self):
        res = perimeter(3.3)
        self.assertEqual(res, 13.2)

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)


if __name__ == '__main__':
    unittest.main()
