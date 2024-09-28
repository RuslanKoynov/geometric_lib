import unittest
import time
import circle
import rectangle
import square
import triangle


class CircleTestCase(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        # time.sleep(1)
        t = time.time() - self.startTime
        print('%s: %.3f' % (self.id(), t))

    def test_less_than_zero(self):
        area = circle.area(-12)
        perimetr = circle.perimeter(-12)
        self.assertEqual(area, "Input data ERROR: radius cannot be negative or zero")
        self.assertEqual(perimetr, "Input data ERROR: radius cannot be negative or zero")

    def test_not_number(self):
        area = circle.area("hi")
        perimetr = circle.perimeter("hi")
        self.assertEqual(area, "Input data ERROR: radius must be a number")
        self.assertEqual(perimetr, "Input data ERROR: radius must be a number")

    def test_zero(self):
        area = circle.area(0)
        perimetr = circle.perimeter(0)
        self.assertEqual(area, "Input data ERROR: radius cannot be negative or zero")
        self.assertEqual(perimetr, "Input data ERROR: radius cannot be negative or zero")

    def test_int_type(self):
        area = circle.area(3)
        perimetr = circle.perimeter(3)
        self.assertEqual(area, 28.2743)
        self.assertEqual(perimetr, 18.8496)

    def test_float_type(self):
        area = circle.area(3.12)
        perimetr = circle.perimeter(3.44)
        self.assertEqual(area, 30.5815)
        self.assertEqual(perimetr, 21.6142)

    def test_bool_type(self):
        area = circle.area(True)
        perimetr = circle.perimeter(False)
        self.assertEqual(area, "Input data ERROR: radius must be a number")
        self.assertEqual(perimetr, "Input data ERROR: radius must be a number")


class RectangleTestCase(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print('%s: %.3f' % (self.id(), t))

    def test_less_than_zero(self):
        area = rectangle.area(-1, 321)
        perimetr = rectangle.perimeter(-100, -901)
        self.assertEqual(area, "Input data ERROR: sides cannot be negative or zero")
        self.assertEqual(perimetr, "Input data ERROR: sides cannot be negative or zero")

    def test_zero(self):
        area = rectangle.area(0, 5)
        perimetr = rectangle.perimeter(5, 0)
        self.assertEqual(area, "Input data ERROR: sides cannot be negative or zero")
        self.assertEqual(perimetr, "Input data ERROR: sides cannot be negative or zero")

    def test_not_number(self):
        area = rectangle.area(19, "hi")
        perimetr = rectangle.perimeter("hi", 100)
        self.assertEqual(area, "Input data ERROR: sides must be a number")
        self.assertEqual(perimetr, "Input data ERROR: sides must be a number")

    def test_int_type(self):
        area = rectangle.area(2, 3)
        perimetr = rectangle.perimeter(8, 8)
        self.assertEqual(area, 6)
        self.assertEqual(perimetr, 32)

    def test_float_type(self):
        area = rectangle.area(15.3, 13)
        perimetr = rectangle.perimeter(15.3, 13)
        self.assertEqual(area, 198.9)
        self.assertEqual(perimetr, 56.6)

    def test_bool_type(self):
        area = rectangle.area(True, 10)
        perimetr = rectangle.perimeter(10, False)
        self.assertEqual(area, "Input data ERROR: sides must be a number")
        self.assertEqual(perimetr, "Input data ERROR: sides must be a number")


class SquareTestCase(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print('%s: %.3f' % (self.id(), t))

    def test_less_than_zero(self):
        area = square.area(-1)
        perimetr = square.perimeter(-100)
        self.assertEqual(area, "Input data ERROR: sides cannot be negative or zero")
        self.assertEqual(perimetr, "Input data ERROR: sides cannot be negative or zero")

    def test_zero(self):
        area = square.area(0)
        perimetr = square.perimeter(0)
        self.assertEqual(area, "Input data ERROR: sides cannot be negative or zero")
        self.assertEqual(perimetr, "Input data ERROR: sides cannot be negative or zero")

    def test_not_number(self):
        area = square.area("hi")
        perimetr = square.perimeter("hi")
        self.assertEqual(area, "Input data ERROR: sides must be a number")
        self.assertEqual(perimetr, "Input data ERROR: sides must be a number")

    def test_int_type(self):
        area = square.area(2)
        perimetr = square.perimeter(8)
        self.assertEqual(area, 4)
        self.assertEqual(perimetr, 32)

    def test_float_type(self):
        area = square.area(15.3)
        perimetr = square.perimeter(15.3)
        self.assertEqual(area, 234.09)
        self.assertEqual(perimetr, 61.2)

    def test_bool_type(self):
        area = square.area(True)
        perimetr = square.perimeter(False)
        self.assertEqual(area, "Input data ERROR: sides must be a number")
        self.assertEqual(perimetr, "Input data ERROR: sides must be a number")


class TriangleTestCase(unittest.TestCase):
    def setUp(self):
        self.startTime = time.time()

    def tearDown(self):
        t = time.time() - self.startTime
        print('%s: %.3f' % (self.id(), t))

    def test_less_than_zero(self):
        area = triangle.area(-1, 10)
        perimetr = triangle.perimeter(-100, 19, -10000)
        self.assertEqual(area, "Input data ERROR: sides cannot be negative or zero")
        self.assertEqual(perimetr, "Input data ERROR: sides cannot be negative or zero")

    def test_zero(self):
        area = triangle.area(0, 9)
        perimetr = triangle.perimeter(1, 0, 8)
        self.assertEqual(area, "Input data ERROR: sides cannot be negative or zero")
        self.assertEqual(perimetr, "Input data ERROR: sides cannot be negative or zero")

    def test_not_number(self):
        area = triangle.area("hi", 12)
        perimetr = triangle.perimeter(12, "hi", 3)
        self.assertEqual(area, "Input data ERROR: sides must be a number")
        self.assertEqual(perimetr, "Input data ERROR: sides must be a number")

    def test_int_type(self):
        area = triangle.area(12, 6)
        perimetr = triangle.perimeter(5, 8, 10)
        self.assertEqual(area, 36)
        self.assertEqual(perimetr, 23)

    def test_float_type(self):
        area = triangle.area(15.3, 16.0)
        perimetr = triangle.perimeter(15.3, 13.4, 6.986)
        self.assertEqual(area, 122.4)
        self.assertEqual(perimetr, 35.686)

    def test_bool_type(self):
        area = triangle.area(True, 90)
        perimetr = triangle.perimeter(3, False, 9)
        self.assertEqual(area, "Input data ERROR: sides must be a number")
        self.assertEqual(perimetr, "Input data ERROR: sides must be a number")

    def test_not_triangle(self):
        area = triangle.area(10, 90)
        perimetr = triangle.perimeter(3, 90, 9)
        self.assertEqual(area, 450)
        self.assertEqual(perimetr, "ERROR: this is not a triangle")
