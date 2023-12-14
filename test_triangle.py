import unittest
from triangle import area
from triangle import perimeter


class TestTriangleArea(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(0,1), 0)
    def test_area(self):
        self.assertAlmostEqual(area(1,2), 1)
    def test_area(self):
        self.assertAlmostEqual(area(3,4), 6)
    def test_area(self):
        self.assertAlmostEqual(area(35616533,83274987), 35616533*83274987/2)

class TestTrianglePerimeter(unittest.TestCase):
    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(0,1,2),3)
    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(1,2,3), 6)
    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(3,4,5), 12)
    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(35616533,83274987,98473),35616533+83274987+98473)
