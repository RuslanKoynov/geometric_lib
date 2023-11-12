import unittest
import circle
import rectangle
import square
import triangle


class CircleTestCaseArea(unittest.TestCase):
    def testInvalidArgument(self):
        self.assertEqual(circle.area(-1), -1)

    def testSimpleRadius(self):
        self.assertEqual(circle.area(3), 28.274333882308138)

    def testZeroRadius(self):
        self.assertEqual(circle.area(0), 0)

    def testBigRadius(self):
        self.assertEqual(circle.area(10_000), 314159265.3589793)


class CircleTestCasePerimeter(unittest.TestCase):
    def testInvalidArgument(self):
        self.assertEqual(circle.perimeter(-1), -1)

    def testSimpleRadius(self):
        self.assertEqual(circle.perimeter(3), 18.84955592153876)

    def testZeroRadius(self):
        self.assertEqual(circle.perimeter(0), 0)

    def testBigRadius(self):
        self.assertEqual(circle.perimeter(10_000), 62831.853071795864)


class RectangleTestCaseArea(unittest.TestCase):
    def testInvalidArgument(self):
        self.assertEqual(rectangle.area(-1, -2), -1)

    def testSimpleSides(self):
        self.assertEqual(rectangle.area(11, 20), 220)

    def testZeroSides(self):
        self.assertEqual(rectangle.area(0, 0), 0)

    def testZeroSide(self):
        self.assertEqual(rectangle.area(0, 100), 0)

    def testBigSides(self):
        self.assertEqual(rectangle.area(10_000, 12345), 123_450_000)


class RectangleTestCasePerimeter(unittest.TestCase):
    def testInvalidArgument(self):
        self.assertEqual(rectangle.perimeter(-1, -2), -1)

    def testSimpleSides(self):
        self.assertEqual(rectangle.perimeter(13, 14), 54)

    def testZeroSide(self):
        self.assertEqual(rectangle.perimeter(0, 20), 20)

    def testZeroSides(self):
        self.assertEqual(rectangle.perimeter(0, 0), 0)

    def testPerimeterBigSides(self):
        self.assertEqual(rectangle.perimeter(10_001, 33_333), 86_668)


class SquareTestCaseArea(unittest.TestCase):
    def testInvalidArgument(self):
        self.assertEqual(square.area(-1), -1)

    def testSimpleSides(self):
        self.assertEqual(square.area(3), 9)

    def testZeroSides(self):
        self.assertEqual(square.area(0), 0)

    def testBigSides(self):
        self.assertEqual(square.area(10_000), 100_000_000)


class SquareTestCasePerimeter(unittest.TestCase):
    def testInvalidArgument(self):
        self.assertEqual(square.perimeter(-1), -1)

    def testSimpleSides(self):
        self.assertEqual(square.perimeter(5), 20)

    def testZeroSides(self):
        self.assertEqual(square.perimeter(0), 0)

    def testBigSides(self):
        self.assertEqual(square.perimeter(20_000), 80_000)


class TriangleTestCaseArea(unittest.TestCase):
    def testInvalidArgument(self):
        self.assertEqual(triangle.area(-1, -1), -1)

    def testOddHeight(self):
        self.assertEqual(triangle.area(3, 3), 4.5)

    def testEvenHeight(self):
        self.assertEqual(triangle.area(3, 4), 6)

    def testZeroSide(self):
        self.assertEqual(triangle.area(0, 4), 0)

    def testBigSide(self):
        self.assertEqual(triangle.area(10_000, 34), 170_000)


class TriangleTestCasePerimeter(unittest.TestCase):
    def testInvalidArgument(self):
        self.assertEqual(triangle.perimeter(-1, -1, -1), -1)

    def testSimpleSides(self):
        self.assertEqual(triangle.perimeter(10, 20, 30), 60)

    def testZeroSides(self):
        self.assertEqual(triangle.perimeter(0, 0, 0), 0)

    def testBigSides(self):
        self.assertEqual(triangle.perimeter(10_000, 4_000, 25_000), 39_000)


if __name__ == "__main__":
    unittest.main()
