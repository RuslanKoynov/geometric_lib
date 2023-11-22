import unittest
import triangle


class TriangleTestCase(unittest.TestCase):
    def tests(self):
        self.assertFalse(triangle.area(0, 2) == 5)
        self.assertFalse(triangle.area(4, 0), 34)
        self.assertNotEqual(triangle.perimeter(0, 5, 5), 10)
        self.assertNotEqual(triangle.perimeter(0, 0, 5), 5)
        self.assertEqual(triangle.area(6, 5), 15)
        self.assertEqual(triangle.area(2, 10), 10)
        self.assertEqual(triangle.area(8, 2), 8)
        self.assertFalse(triangle.area(1, 4) == 3)
        self.assertEqual(triangle.perimeter(5, 6, 7), 18)
        self.assertNotEqual(triangle.perimeter(-5, 5, 4), 4)
        self.assertFalse(triangle.perimeter(3, 43, 6) == triangle.perimeter(-3, 46, 6))
        self.assertTrue(triangle.perimeter(1, 2, 4) == triangle.perimeter(4, 2, 1))
