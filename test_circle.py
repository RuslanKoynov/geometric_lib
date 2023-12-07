import unittest
from circle import area
from circle import perimeter
class CircleTestCase(unittest.TestCase):
    def test_1_area(self):
        result = area(4)
        self.assertEqual(result, 50.26548)
    def test_2_area(self):
        result = area(21)
        self.assertEqual(result, 1385.44236)
    def test_3_area(self):
        with self.assertRaises(ValueError) as context:
            result = area(-9)
    def test_1_perimeter(self):
        result = perimeter(3)
        self.assertEqual(result, 18.84956)
    def test_2_perimeter(self):
        result = perimeter(11)
        self.assertEqual(result, 69.11504)
    def test_3_perimeter(self):
        result = perimeter(5)
        self.assertEqual(result, 31.41593)

if __name__ == '__main__':
    unittest.main()