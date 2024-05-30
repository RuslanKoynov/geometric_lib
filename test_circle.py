import unittest
from circle import area, perimeter
import math

class CircleTestCase(unittest.TestCase):
    def test_area_normal(self):
        self.assertAlmostEqual(area(5), math.pi * 25)

    def test_perimeter_normal(self):
        self.assertAlmostEqual(perimeter(5), 2 * math.pi * 5)

if __name__ == '__main__':
    unittest.main()
