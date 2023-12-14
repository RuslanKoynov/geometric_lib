import unittest


from rectangle import area
from rectangle import perimeter

class RectangleTest(unittest.TestCase):
    def test_rectangle_area_1(self):
        res = area(0, 5)
        self.assertEqual(res, 0)

    def test_rectangle_area_2(self):
        res = area(5, 5)
        self.assertEqual(res, 25)

    def test_rectangle_area_3(self):
        res = area(-5, -5)
        self.assertEqual(res, "Error negative value")

    def test_rectangle_area_4(self):
        res = area("5", "5")
        try:
            perimeter("5","5")
        except TypeError:
            print("Error str")

    def test_rectangle_perimeter_1(self):
        res = perimeter(5, 0)
        self.assertEqual(res,0)

    def test_rectangle_perimeter_2(self):
        res = perimeter(1, 5)
        self.assertEqual(res, 12)

    def test_rectangle_perimeter_3(self):
        res = perimeter(-1, -2)
        self.assertEqual(res, "Error negative value")

    def test_rectangle_perimeter_4(self):
        res = perimeter("1", "1")
        try:
            perimeter("1","1")
        except TypeError:
            print("Error str")