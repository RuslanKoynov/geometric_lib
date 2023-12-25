import unittest
from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):
    def test_rectangle_zero_area(self):
        res = area(0, 0)
        self.assertEqual(res, 0)

    def test_rectangle_rational_area(self):
        res = area(3.5, 4.5)
        self.assertEqual(res, 15.75)

    def test_rectangle_negative_area(self):
        self.assertRaises(ValueError, area, -3, -4)

    def test_rectangle_positive_area(self):
        res = area(3, 4)
        self.assertEqual(res, 12)

    def test_rectangle_other_data_type_area(self):
        self.assertRaises(TypeError, area, "123", "123")

    def test_rectangle_zero_perimeter(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_rectangle_rational_perimeter(self):
        res = perimeter(3.5, 4.5)
        self.assertEqual(res, 16)

    def test_rectangle_negative_perimeter(self):
        self.assertRaises(ValueError, perimeter, -3, -2)

    def test_rectangle_positive_perimeter(self):
        res = perimeter(3, 4)
        self.assertEqual(res, 14)

    def test_rectangle_other_data_type_perimeter(self):
        self.assertRaises(TypeError, perimeter, "123", "123")

if __name__ == '__main__':
    unittest.main()
