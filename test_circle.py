import unittest
from circle import area
from circle import perimeter
from math import pi

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(0), pi * 0 ** 2 )
    def test_area(self):
        self.assertAlmostEqual(round(area(1),2), pi * 1 ** 2)
    def test_area(self):
        self.assertAlmostEqual(area(3), pi * 3 ** 2)
    def test_area(self):
        self.assertAlmostEqual(area(35616533), pi*35616533**2)

class TestCirclePerimeter(unittest.TestCase):
    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(0), pi * 0 * 2)
    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(1), pi * 1 * 2)
    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(3), pi * 3 * 2)
    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(35616533), pi * 35616533 * 2)

