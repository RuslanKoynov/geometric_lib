import circle, rectangle, square, triangle

import unittest
import math

class CircleAreaTestCase(unittest.TestCase):
    def test_zero(self):
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_big(self):
        res = circle.area(408750)
        self.assertEqual(res, math.pi * 167076562500)

    def test_sample(self):
        res = circle.area(36)
        self.assertEqual(res, math.pi * 1296)

    def test_small(self):
        res = circle.area(1)
        self.assertEqual(res, math.pi)
    
    def test_negative(self):
        res = circle.area(-1)
        self.assertEqual(res, ValueError)

    def test_string(self):
        res = circle.area("Are strings allowed?")
        self.assertEqual(res, ValueError)

class CirclePerimeterTestCase(unittest.TestCase):
    def test_zero(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)

    def test_big(self):
        res = circle.perimeter(408750)
        self.assertEqual(res, math.pi * 817500)

    def test_sample(self):
        res = circle.perimeter(34)
        self.assertEqual(res, math.pi * 68)
    
    def test_small(self):
        res = circle.perimeter(7)
        self.assertEqual(res, math.pi * 14)
    
    def test_negative(self):
        res = circle.perimeter(-2)
        self.assertEqual(res, ValueError)

    def test_string(self):
        res = circle.perimeter("Are str allowed?")
        self.assertEqual(res, ValueError)

class RectangleAreaTestCase(unittest.TestCase):
    def test_zero_height(self):
        res = rectangle.area(0, 2)
        self.assertEqual(res, 0)

    def test_zero_width(self):
        res = rectangle.area(4, 0)
        self.assertEqual(res, 0)

    def test_zero_both(self):
        res = rectangle.area(0, 0)
        self.assertEqual(res, 0)

    def test_big(self):
        res = rectangle.area(408, 750)
        self.assertEqual(res, 306000)
    
    def test_sample(self):
        res = rectangle.area(2, 87)
        self.assertEqual(res, 174)

    def test_small(self):
        res = rectangle.area(1, 1)
        self.assertEqual(res, 1)
    
    def test_negative(self):
        res = rectangle.area(-3, 1)
        self.assertEqual(res, ValueError)

    def test_negative_both(self):
        res = rectangle.area(-3, -3)
        self.assertEqual(res, ValueError)

    def test_string(self):
        res = rectangle.area(1, "Are str allowed?")
        self.assertEqual(res, ValueError)


class RectanglePerimeterTestCase(unittest.TestCase):
    def test_zero_height(self):
        res = rectangle.perimeter(0, 4)
        self.assertEqual(res, ValueError)

    def test_zero_width(self):
        res = rectangle.perimeter(8, 0)
        self.assertEqual(res, ValueError)

    def test_zero_both(self):
        res = rectangle.perimeter(0, 0)
        self.assertEqual(res, ValueError)

    def test_big(self):
        res = rectangle.perimeter(408, 750)
        self.assertEqual(res, 2316)
    
    def test_sample(self):
        res = rectangle.perimeter(2, 87)
        self.assertEqual(res, 178)

    def test_small(self):
        res = rectangle.perimeter(1, 1)
        self.assertEqual(res, 4)
    
    def test_negative(self):
        res = rectangle.perimeter(-33, 1)
        self.assertEqual(res, ValueError)

    def test_negative_both(self):
        res = rectangle.perimeter(-1, -33)
        self.assertEqual(res, ValueError)

    def test_string(self):
        res = rectangle.perimeter(1, "Are str allowed?")
        self.assertEqual(res, ValueError)

class SquareAreaTestCase(unittest.TestCase):
    def test_zero(self):
        res = square.area(0)
        self.assertEqual(res, 0)

    def test_big(self):
        res = square.area(408750)
        self.assertEqual(res, 167076562500)
    
    def test_sample(self):
        res = square.area(33)
        self.assertEqual(res, 1089)

    def test_small(self):
        res = square.area(1)
        self.assertEqual(res, 1)
    
    def test_negative(self):
        res = square.area(-2)
        self.assertEqual(res, ValueError)

    def test_string(self):
        res = square.area("Are str allowed?")
        self.assertEqual(res, ValueError)

class SquarePerimeterTestCase(unittest.TestCase):
    def test_zero(self):
        res = square.perimeter(0)
        self.assertEqual(res, ValueError)

    def test_big(self):
        res = square.perimeter(408750)
        self.assertEqual(res, 1635000)
    
    def test_sample(self):
        res = square.perimeter(33)
        self.assertEqual(res, 132)

    def test_small(self):
        res = square.perimeter(1)
        self.assertEqual(res, 4)
    
    def test_negative(self):
        res = square.perimeter(-2)
        self.assertEqual(res, ValueError)

    def test_string(self):
        res = square.perimeter("Are str allowed?")
        self.assertEqual(res, ValueError)

class TriangleAreaTestCase(unittest.TestCase):
    def test_zero_side(self):
        res = triangle.area(0, 1)
        self.assertEqual(res, 0)
    
    def test_zero_height(self):
        res = triangle.area(1, 0)
        self.assertEqual(res, 0)
    
    def test_sample(self):
        res = triangle.area(2, 4)
        self.assertEqual(res, 4)
    
    def test_negative_side(self):
        res = triangle.area(-42, 4)
        self.assertEqual(res, ValueError)
    
    def test_negative_height(self):
        res = triangle.area(2, -4)
        self.assertEqual(res, ValueError)

    def test_string(self):
        res = triangle.area("Are str allowed?", 5)
        self.assertEqual(res, ValueError)
    
class TrianglePerimeterTestCase(unittest.TestCase):
    def test_zero_side(self):
        res = triangle.perimeter(0, 3, 3)
        self.assertEqual(res, ValueError)

    def test_impossible_sides(self):
        res = triangle.perimeter(1, 10, 2)
        self.assertEqual(res, ValueError)
    
    def test_sample(self):
        res = triangle.perimeter(3, 4, 5)
        self.assertEqual(res, 12)
    
    def test_negative(self):
        res = triangle.perimeter(-2, 4, 3)
        self.assertEqual(res, ValueError)

    def test_string(self):
        res = triangle.perimeter("Are str allowed?", 5, 1)
        self.assertEqual(res, ValueError)
    