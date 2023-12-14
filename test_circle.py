import unittest

from circle import area
from circle import perimeter


class circleTest(unittest.TestCase):
    def test_circle_area_1(self):
        res = area(3)
        self.assertEqual(res, 28.274333882308138)

    def test_circle_area_2(self):
        res = area(-3)
        self.assertEqual(res, "Error negative value")


    def test_circle_area_3(self):
        res = area("3")
        try:
            perimeter("3")
        except TypeError:
            print("Error str")

    def test_circle_area_4(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_circle_perimeter_1(self):
        res = perimeter(3)
        self.assertEqual(res, 18.84955592153876)

    def test_circle_perimeter_2(self):
        res = perimeter(-3)
        self.assertEqual(res, "Error negative value")


    def test_circle_perimeter_3(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_circle_perimeter_4(self):
        res = perimeter("3")
        try:
            perimeter("3")
        except TypeError:
            print("Error str")
