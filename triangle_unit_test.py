import unittest
from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):
    def test_triangle_zero_area(self):
        res = area(0, 0)
        self.assertEqual(res, 0)

    def test_triangle_rational_area(self):
        res = area(3.5, 4.5)
        self.assertEqual(res, 7.875)

    def test_triangle_negative_area(self):
        self.assertRaises(TypeError, area, -3, -4)

    def test_triangle_positive_area(self):
        res = area(3, 4)
        self.assertEqual(res, 6)

    def test_triangle_other_data_type_area(self):
        self.assertRaises(TypeError, area, "123", "123")

    def test_triangle_zero_perimeter(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_triangle_rational_perimeter(self):
        res = perimeter(3.5, 4.5, 5.5)
        self.assertEqual(res, 13.5)

    def test_triangle_negative_perimeter(self):
        self.assertRaises(TypeError, perimeter, -3, -4, -5)

    def test_triangle_positive_perimeter(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_triangle_other_data_type_perimeter(self):
        self.assertRaises(TypeError, perimeter, "123", "123", "123")

if __name__ == '__main__':
    unittest.main()


