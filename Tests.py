import unittest
import circle
import rectangle
import square
import triangle


class CircleTestCase(unittest.TestCase):
    def testAreaLittleRadius(self):
        self.assertEqual(circle.area(3), 28.274333882308138)

    def testZeroRadius(self):
        self.assertEqual(circle.area(0), 0)

    def testAreaBigRadius(self):
        self.assertEqual(circle.area(10_000), 314159265.3589793)

    def testPerimeterLittleRadius(self):
        self.assertEqual(circle.perimeter(3), 18.84955592153876)

    def testPerimeterZeroRadius(self):
        self.assertEqual(circle.perimeter(0), 0)

    def testPerimeterBigRadius(self):
        self.assertEqual(circle.perimeter(10_000), 62831.853071795864)


class RectangleTestCase(unittest.TestCase):
    def testAreaLittleSides(self):
        self.assertEqual(rectangle.area(11, 20), 220)

    def testAreaZeroSides(self):
        self.assertEqual(rectangle.area(0, 0), 0)

    def testtAreaZeroSide(self):
        self.assertEqual(rectangle.area(0, 100), 0)

    def testAreaBigSides(self):
        self.assertEqual(rectangle.area(10_000, 12345), 123_450_000)

    def testPerimeterLittleSides(self):
        self.assertEqual(rectangle.perimeter(13, 14), 54)

    def testPerimeterZeroSide(self):
        self.assertEqual(rectangle.perimeter(0, 20), 20)

    def testPerimeterZeroSides(self):
        self.assertEqual(rectangle.perimeter(0, 0), 0)

    def testPerimeterBigSides(self):
        self.assertEqual(rectangle.perimeter(10_001, 33_333), 86_668)


class SquareTestCase(unittest.TestCase):
    def testAreaLittleSides(self):
        self.assertEqual(square.area(3), 9)

    def testAreaZeroSides(self):
        self.assertEqual(square.area(0), 0)

    def testAreaBigSides(self):
        self.assertEqual(square.area(10_000), 100_000_000)

    def testPerimeterLittleSides(self):
        self.assertEqual(square.perimeter(5), 20)

    def testPerimeterZeroSides(self):
        self.assertEqual(square.perimeter(0), 0)

    def testPerimeterBigSides(self):
        self.assertEqual(square.perimeter(20_000), 80_000)


class TriangleTestCase(unittest.TestCase):
    def testAreaOddHeight(self):
        self.assertEqual(triangle.area(3, 3), 4.5)

    def testAreaEvenHeight(self):
        self.assertEqual(triangle.area(3, 4), 6)

    def testAreaZeroSide(self):
        self.assertEqual(triangle.area(0, 4), 0)

    def testAreaBigSide(self):
        self.assertEqual(triangle.area(10_000, 34), 170_000)

    def testPerimeterLittleSides(self):
        self.assertEqual(triangle.perimeter(10, 20, 30), 60)

    def testPerimeterZeroSides(self):
        self.assertEqual(triangle.perimeter(0, 0, 0), 0)

    def testPerimeterBigSides(self):
        self.assertEqual(triangle.perimeter(10_000, 4_000, 25_000), 39_000)


if __name__ == "__main__":
    unittest.main()
