import unittest
from rectangle import area
from rectangle import perimeter
class RectangleTestCase(unittest.TestCase):
    def test_1_area(self):
        result = area(7, 4)
        self.assertEqual(result, 28)
    def test_2_area(self):
        result = area(3, 10)
        self.assertEqual(result, 30)
    def test_3_area(self):
        with self.assertRaises(ValueError) as context:
            result = area(23, 0)
    def test_1_perimeter(self):
        result = perimeter(5, 6)
        self.assertEqual(result, 22)
    def test_2_perimeter(self):
        with self.assertRaises(ValueError) as context:
            result = perimeter(45, -7)
    def test_3_perimeter(self):
        result = perimeter(2, 1)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()