import unittest
from triangle import area
from triangle import perimeter


class TestTriangleArea(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(area(0,1), 0*1/2)
    def test_area(self):
        self.assertAlmostEqual(area(1,2), 1*2/2)
    def test_area(self):
        self.assertAlmostEqual(area(3,4), 3*4/2)
    def test_area(self):
        self.assertAlmostEqual(area(35616533,83274987), 35616533*83274987/2)

class TestTrianglePerimeter(unittest.TestCase):
    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(0,1,2),0+1+2)
    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(1,2,3), 1+2+3)
    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(3,4,5), 3+4+5)
    def test_perimeter(self):
        self.assertAlmostEqual(perimeter(35616533,83274987,98473),35616533+83274987+98473)

