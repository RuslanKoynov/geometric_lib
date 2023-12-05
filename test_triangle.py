import unittest
from triangle import area
from triangle import perimeter
class TriangleTestCase(unittest.TestCase):
    def test_1_area(self):
        result = area(3, 9)
        self.assertEqual(result, 13.5)
    def test_2_area(self):
        with self.assertRaises(ValueError) as context:
            result = area(34, -3)
        self.assertRaises(ValueError, result)
    def test_3_area(self):
        with self.assertRaises(ValueError) as context:
            result = area(0, 6)
        self.assertRaises(ValueError, result)
    def test_1_perimeter(self):
        result = perimeter(4, 7, 10)
        self.assertEqual(result, 21)
    def test_2_perimeter(self):
        with self.assertRaises(ValueError) as context:
            result = perimeter(9, -8, 3)
        self.assertRaises(ValueError, result)
    def test_3_perimeter(self):
        result = perimeter(11, 14, 18)
        self.assertEqual(result, 43)

if __name__ == '__main__':
    unittest.main()