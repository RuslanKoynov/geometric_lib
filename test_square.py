import unittest
from square import area
from square import perimeter


class TestSquareArea(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(0), 0**2)
        self.assertEqual(area(1), 1**2)
        self.assertEqual(area(3), 3**2)
        self.assertEqual(area(35616533), 35616533**2)

class TestSquarePerimeter(unittest.TestCase):
    def test_perimeter(self):
        self.assertEqual(perimeter(0), 4*0)
        self.assertEqual(perimeter(1), 4*1)
        self.assertEqual(perimeter(3), 4*3)
        self.assertEqual(perimeter(35616533), 4*35616533)

