import unittest
import rectangle

class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)

    def test_positive_area(self):
        with self.assertRaises(ValueError):
            res = rectangle.area(0)

    def test_negative_side_rectangle_area(self):
        with self.assertRaises(ValueError):
            res = rectangle.area(0)

    def test_zero_perimeter(self):
        with self.assertRaises(ValueError):
            res = rectangle.perimetr(0)

    def test_square_perimeter(self):
        res = rectangle.perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_negative_side_rectangle_perimetr(self):
        with self.assertRaises(ValueError):
            res = rectangle.area(0)
