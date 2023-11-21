from triangle import area, perimeter
import unittest

class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 3)
        self.assertEqual(res, 15)

    def test_square_mul(self):
        res = area(4, 2)
        self.assertEqual(res, 4)

    def test_zero_mul(self):
        res = area(50, 10)
        self.assertEqual(res, 250)

    def test_square_mul(self):
        res = area(-9, 5)
        self.assertEqual(res, "ERROR")

    def test_zero_mul(self):
        res = perimeter(10, 4,5)
        self.assertEqual(res, "ERROR")

    def test_square_mul(self):
        res = perimeter(2, 4,3)
        self.assertEqual(res, 9)

    def test_zero_mul(self):
        res = perimeter(30, 36, 22)
        self.assertEqual(res, 88)

    def test_square_mul(self):
        res = perimeter(1, 1, -1)
        self.assertEqual(res, "ERROR")

if  __name__ == "__main__":
    unittest.main()



