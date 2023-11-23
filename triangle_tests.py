import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    def test_area_positive(self):
        res = area(6, 3)
        self.assertEqual(res, 9.0)

    def test_area_negative(self):
        res = area(10, -8)
        self.assertEqual(res, "None")

    def test_area_real(self):
        res = area(10.1, 1.10)
        self.assertEqual(res, 5.555)

    def test_area_zero(self):
        res = area(8, 0)
        self.assertEqual(res, 0)

    def test_perimeter_positive(self):
        res = perimeter(10, 10, 11)
        self.assertEqual(res, 31)

    def test_perimeter_negative(self):
        res = perimeter(8, -3, 4)
        self.assertEqual(res, "None")

    def test_perimeter_real(self):
        res = perimeter(10.1, 1.10, 9.9)
        self.assertEqual(res, 21.1)

    def test_perimeter_zero(self):
        res = perimeter(6, 0, 6.6)
        self.assertEqual(res, 0)


if __name__ == '__main__':
    unittest.main()
