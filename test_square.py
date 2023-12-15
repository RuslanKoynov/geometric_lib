import unittest
from square import area
from square import perimeter


class TestSquareArea(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(0), 0)
    def test_area(self):
        self.assertAlmostEqual(area(1), 1)
    def test_area(self):
        self.assertRaises(ValueError,area, -3)
    def test_area(self):
        self.assertAlmostEqual(area(35616533), 126854801372569)

class TestSquarePerimeter(unittest.TestCase):
    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(0), 0)
    def test_perimeter(self):
        self.assertvEqual(perimeter(1), 4)
    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(3), 12)
    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(35616533), 142466132)
