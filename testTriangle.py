from triangle import perimeter, area
import unittest

class TriangleTest(unittest.TestCase):

    def test_area_Triangle_Five_Two(self):
        res = area(1.3,2)
        self.assertEqual(res, 1.3)

    def test_area_Triangle_Seven_Four(self):
        res = area(7,4)
        self.assertEqual(res, 14.0)

    def test_area_Triangle_Nine_Three(self):
        res = area(9,3)
        self.assertEqual(res, 13.5)

    def test_perimeter_Triangle_Two_Three_Four(self):
        res = perimeter(2,3,4)
        self.assertEqual(res, 9)

    def test_perimeter_Triangle_MinusSeven_One_Sixth(self):
        res = perimeter(-7,1,6)
        self.assertEqual(res, "ERROR")

    def test_perimeter_Triangle_Sixth_One_Seven(self):
        res = perimeter (6,1,7)
        self.assertEqual(res, 14)