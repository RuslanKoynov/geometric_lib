import unittest
from square import area
from square import perimeter
class SquareTestCase(unittest.TestCase):
    def test_1_area(self):
        with self.assertRaises(ValueError) as context:
            result = area(-7)
    def test_2_area(self):
        with self.assertRaises(ValueError) as context:
            result = area(0)
    def test_3_area(self):
        result = area(72)
        self.assertEqual(result, 5184)
    def test_1_perimeter(self):
        with self.assertRaises(ValueError) as context:
            result = perimeter(-8)
    def test_2_perimeter(self):
        result = perimeter(23)
        self.assertEqual(result, 92)
    def test_3_perimeter(self):
        result = perimeter(49)
        self.assertEqual(result, 196)

if __name__ == '__main__':
    unittest.main()