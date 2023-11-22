import math
import unittest
import circle


class CircleTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(circle.area(0), 0)
        self.assertEqual(circle.perimeter(0), 0)
        self.assertFalse(circle.perimeter(0) == 239)
        self.assertFalse(circle.area(0) == 239)
        self.assertEqual(circle.area(5), 25 * math.pi)
        self.assertFalse(circle.area(-2) == 4 * math.pi)
        self.assertEqual(circle.area(1), math.pi)
        self.assertNotEquals(circle.area(-1), math.pi)
        self.assertNotEquals(circle.perimeter(3), 10 * math.pi)
        self.assertTrue(circle.area(6) == 36 * math.pi)
        self.assertTrue(circle.perimeter(2) == 4 * math.pi)
        self.assertFalse(circle.area(8) == 25 * 3.14)
        self.assertTrue(circle.area(8) == circle.area(8))
        self.assertEqual(circle.perimeter(2), circle.area(2))
