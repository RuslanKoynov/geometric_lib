import unittest
import square


class SquareTest(unittest.TestCase):
    def tests(self):
        self.assertTrue(square.area(0) == 0)
        self.assertEqual(square.area(0), 0)
        self.assertFalse(square.area(0) == 3)
        self.assertNotEqual(square.area(0), 8)
        self.assertFalse(square.area(4) == 0)
        self.assertEqual(square.area(8), 64)
        self.assertNotEqual(square.area(-8), 64)
        self.assertFalse(square.area(5) == 34)
        self.assertEqual(square.perimeter(10), 40)
        self.assertNotEqual(square.perimeter(-5), 20)
        self.assertFalse(square.perimeter(2) == 7)
        self.assertNotEqual(square.perimeter(8), square.perimeter(-8))