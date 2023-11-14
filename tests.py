import unittest
from math import pi

import circle
import rectangle
import square
import triangle


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = rectangle.area(10, 10)
        self.assertEqual(res, 100)

    def test_zero_perimetr(self):
        res = rectangle.perimeter(10, 0)
        self.assertEqual(res, 20)

    def test_square_perimetr(self):
        res = rectangle.perimeter(10, 10)
        self.assertEqual(res, 40)


class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = circle.area(10)
        self.assertEqual(res, 100 * pi)

    def test_zero_perimetr(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_square_perimetr(self):
        res = circle.perimeter(10)
        self.assertEqual(res, 2 * pi * 10)


class SquareTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = square.area(10)
        self.assertEqual(res, 100)

    def test_zero_perimetr(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)

    def test_square_perimetr(self):
        res = square.perimeter(10)
        self.assertEqual(res, 40)


class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = triangle.area(0, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = triangle.area(4, 8)
        self.assertEqual(res, 16)

    def test_zero_perimetr(self):
        res = triangle.perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_square_perimetr(self):
        res = triangle.perimeter(10, 10, 15)
        self.assertEqual(res, 35)
