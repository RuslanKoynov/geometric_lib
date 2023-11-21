import unittest
from square import area, perimeter
import unittest

class SquareTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_square_mul(self):
        res = area(13)
        self.assertEqual(res, 169)

    def test_zero_mul(self):
        res = area(1)
        self.assertEqual(res, 1)

    def test_square_mul(self):
        res = area(-8)
        self.assertEqual(res, "ERROR")

    def test_zero_mul(self):
        res = perimeter(10)
        self.assertEqual(res, 40)

    def test_square_mul(self):
        res = perimeter(51)
        self.assertEqual(res, 204)

    def test_zero_mul(self):
        res = perimeter(3)
        self.assertEqual(res, 12)

    def test_square_mul(self):
        res = perimeter(-99)
        self.assertEqual(res, "ERROR")

if  __name__ == "__main__":
    unittest.main()
