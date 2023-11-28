import unittest
from triangle import area
from triangle import perimeter


class TestTriangleArea(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(0,1), 0*1/2)
        self.assertEqual(area(1,2), 1*2/2)
        self.assertEqual(area(3,4), 3*4/2)
        self.assertEqual(area(35616533,83274987), 35616533*83274987/2)

class TestTrianglePerimeter(unittest.TestCase):
    def test_perimeter(self):
        self.assertEqual(perimeter(0,1,2),0+1+2)
        self.assertEqual(perimeter(1,2,3), 1+2+3)
        self.assertEqual(perimeter(3,4,5), 3+4+5)
        self.assertEqual(perimeter(35616533,83274987,98473),35616533+83274987+98473)

