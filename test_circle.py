import unittest
from circle import area
from circle import perimeter
class CircleTestCase(unittest.TestCase):
    def test_1_area(self):
        result = area(4)
        self.assertAlmostEqual(result, 50.26548, delta = 0.001)
    def test_2_area(self):
        result = area(21)
        self.assertAlmostEqual(result, 1385.44236, delta = 0.001)
    def test_3_area(self):
        with self.assertRaises(ValueError) as context:
            result = area(-9)
    def test_1_perimeter(self):
        result = perimeter(3)
        self.assertAlmostEqual(result, 18.84956, delta = 0.001)
    def test_2_perimeter(self):
        result = perimeter(11)
        self.assertAlmostEqual(result, 69.11504, delta = 0.001)
    def test_3_perimeter(self):
        result = perimeter(5)
        self.assertAlmostEqual(result, 31.41593, delta = 0.001)

if __name__ == '__main__':
    unittest.main()