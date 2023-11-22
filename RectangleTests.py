import unittest
import rectangle


class RectangleTestCase(unittest.TestCase):
    def tests(self):
        self.assertEqual(rectangle.area(1210, 0), 0)
        self.assertEqual(rectangle.area(0, 454), 0)
        self.assertFalse(rectangle.area(0, 10) == 239)
        self.assertEqual(rectangle.area(10, 10), 100)
        self.assertFalse(rectangle.area(-1, 1) == rectangle.area(1, -1))
        self.assertFalse(rectangle.area(2, -2) == rectangle.area(-2, 2))
        self.assertEqual(rectangle.area(2, 5), 10)
        self.assertFalse(rectangle.area(2, 3) == 102)
        self.assertEqual(rectangle.perimeter(10, 10), 40)
        self.assertNotEquals(rectangle.perimeter(0, 123), 246)
        self.assertFalse(rectangle.perimeter(-239, -84) == rectangle.perimeter(239, 84))
        self.assertEqual(rectangle.perimeter(5, 2), 14)
        self.assertFalse(rectangle.perimeter(2, 3) == 7)
        self.assertEqual(rectangle.perimeter(0, 0), 0)
        self.assertFalse(rectangle.perimeter(-5, 10) == rectangle.perimeter(2, 3))