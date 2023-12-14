import unittest
from circle import area
from circle import perimeter
from math import pi

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(0), 0)
    def test_area(self):
        self.assertAlmostEqual(area(1), 3.14)
    def test_area(self):
        self.assertAlmostEqual(area(3), 28.26)
    def test_area(self):
        self.assertAlmostEqual(area(35616533), 3.98321e15)

class TestCirclePerimeter(unittest.TestCase):
    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(0), 0)
    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(1), 6.28)
    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(3), 18.84)
    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(35616533), 223671827)

