import circle
import rectangle
import square
import triangle
import unittest
import math


class CircleAreaTestCase(unittest.TestCase):
    def test_small(self):
        res = circle.area(7)
        self.assertEqual(res, 153.93804002589985)

    def test_zero(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_big(self):
        res = circle.area(36)
        self.assertEqual(res, math.pi * 1296)

    def test_neg(self):
        res = circle.area(-7)
        self.assertEqual(res, ValueError)


class CirclePerimeterTestCase(unittest.TestCase):
    def test_zero(self):
        res = circle.perimeter(0)
        self.assertEqual(res, ValueError)

    def test_big(self):
        res = circle.perimeter(36)
        self.assertEqual(res, math.pi * 72)

    def test_small(self):
        res = circle.perimeter(7)
        self.assertEqual(res, math.pi * 14)

    def test_neg(self):
        res = circle.perimeter(-7)
        self.assertEqual(res, ValueError)


class RectangleAreaTestCase(unittest.TestCase):
    def test_zero(self):
        res = rectangle.area(0, 5)
        self.assertEqual(res, ValueError)

    def test_small(self):
        res = rectangle.area(2, 5)
        self.assertEqual(res, 10)

    def test_big(self):
        res = rectangle.area(408, 750)
        self.assertEqual(res, 306000)

    def test_neg(self):
        res = rectangle.area(-2, 5)
        self.assertEqual(res, ValueError)


class RectanglePerimeterTestCase(unittest.TestCase):

    def test_zero(self):
        res = rectangle.perimeter(2, 0)
        self.assertEqual(res, ValueError)

    def test_small(self):
        res = rectangle.perimeter(2, 5)
        self.assertEqual(res, 14)

    def test_big(self):
        res = rectangle.perimeter(408, 750)
        self.assertEqual(res, 2316)

    def test_neg(self):
        res = rectangle.perimeter(-2, 5)
        self.assertEqual(res, ValueError)


class SquareAreaTestCase(unittest.TestCase):

    def test_zero(self):
        res = square.area(0)
        self.assertEqual(res, ValueError)

    def test_big(self):
        res = square.area(408750)
        self.assertEqual(res, 167076562500)

    def test_small(self):
        res = square.area(6)
        self.assertEqual(res, 36)

    def test_neg(self):
        res = square.area(-6)
        self.assertEqual(res, ValueError)


class SquarePerimeterTestCase(unittest.TestCase):
    def test_zero(self):
        res = square.perimeter(0)
        self.assertEqual(res, ValueError)

    def test_big(self):
        res = square.perimeter(408750)
        self.assertEqual(res, 1635000)

    def test_small(self):
        res = square.perimeter(6)
        self.assertEqual(res, 36)

    def test_neg(self):
        res = square.perimeter(-6)
        self.assertEqual(res, ValueError)


class TriangleAreaTestCase(unittest.TestCase):

    def test_zero(self):
        res = triangle.area(0, 1)
        self.assertEqual(res, ValueError)

    def test_big(self):
        res = triangle.area(20, 40)
        self.assertEqual(res, 400)

    def test_small(self):
        res = triangle.area(5, 10)
        self.assertEqual(res, 25)

    def test_neg(self):
        res = triangle.area(-5, 10)
        self.assertEqual(res, ValueError)


class TrianglePerimeterTestCase(unittest.TestCase):

    def test_zero(self):
        res = triangle.perimeter(0, 5, 2)
        self.assertEqual(res, ValueError)

    def test_impossible(self):
        res = triangle.perimeter(1, 10, 2)
        self.assertEqual(res, ValueError)

    def test_sample(self):
        res = triangle.perimeter(7, 5, 2)
        self.assertEqual(res, 14)

    def test_neg(self):
        res = triangle.perimeter(-7, -5, -2)
        self.assertEqual(res, ValueError)
