import unittest
from square import area
from square import perimeter


class TestSquareArea(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(0), 0**2)
    def test_area(self):
        self.assertAlmostEqual(area(1), 1**2)
    def test_area(self):
        self.assertAlmostEqual(area(3), 3**2)
    def test_area(self):
        self.assertAlmostEqual(area(35616533), 35616533**2)

class TestSquarePerimeter(unittest.TestCase):
    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(0), 4*0)
    def test_perimeter(self):
        self.assertvEqual(perimeter(1), 4*1)
    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(3), 4*3)
    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(35616533), 4*35616533)

