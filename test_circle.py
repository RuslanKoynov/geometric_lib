import unittest
from circle import area
from circle import perimeter
from math import pi

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(0), pi * 0 ** 2)
    def test_area(self):
        self.assertEqual(area(1), pi * 1 ** 2)
    def test_area(self):
        self.assertEqual(area(3), pi * 3 ** 2)
    def test_area(self):
        self.assertEqual(area(35616533), pi*35616533**2)

class TestCirclePerimeter(unittest.TestCase):
    def test_perimeter(self):
        self.assertEqual(perimeter(0), pi * 0 * 2)
    def test_perimeter(self):
        self.assertEqual(perimeter(1), pi * 1 * 2)
    def test_perimeter(self):
        self.assertEqual(perimeter(3), pi * 3 * 2)
    def test_perimeter(self):
        self.assertEqual(perimeter(35616533), pi * 35616533 * 2)

