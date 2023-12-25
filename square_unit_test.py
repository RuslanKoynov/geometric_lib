import unittest
from square import area, perimeter

class SquareTestCase(unittest.TestCase):
    def test_square_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_square_rational_area(self):
        res = area(3.5)
        self.assertEqual(res, 12.25)

    def test_square_negative_area(self):
        self.assertRaises(ValueError, area, -3)

    def test_square_positive_area(self):
        res = area(3)
        self.assertEqual(res, 9)

    def test_square_other_data_type_area(self):
        self.assertRaises(TypeError, area, "123")

    def test_square_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_square_rational_perimeter(self):
        res = perimeter(3.5)
        self.assertEqual(res, 14)

    def test_square_negative_perimeter(self):
        self.assertRaises(ValueError, perimeter, -3)

    def test_square_positive_perimeter(self):
        res = perimeter(3)
        self.assertEqual(res, 12)

    def test_square_other_data_type_perimeter(self):
        self.assertRaises(TypeError, perimeter, "123")

if __name__ == '__main__':
    unittest.main()
