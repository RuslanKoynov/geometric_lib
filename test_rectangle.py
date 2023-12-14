import unittest
from rectangle import area
from rectangle import perimeter


class TestRectangleArea(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(0,1), 0)
    def test_area(self):
        self.assertAlmostEqual(area(1,2), 2)
    def test_area(self):
        self.assertRaises(ValueError,area, -3, -4)
    def test_area(self):
        self.assertAlmostEqual(area(35616533,38749), 49154682837587)

class TestRectanglePerimeter(unittest.TestCase):
    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(0, 1), 2)
    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(1, 2), 6)
    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(3, 4), 14)
    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(35616533, 38749), 71310564)
