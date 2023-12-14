import unittest


from triangle import area
from triangle import perimeter

class triangleTest(unittest.TestCase):
    def test_triangle_area_1(self):
        res = area(0, 5)
        self.assertEqual(res, 0)

    def test_triangle_area_2(self):
        res = area(5, 2)
        self.assertEqual(res, 5)

    def test_triangle_area_3(self):
        res = area(-5, -5)
        self.assertEqual(res, "Error negative value")

    def test_triangle_area_4(self):
        res = area("5", "2")
        try:
            perimeter("5","2")
        except TypeError:
            print("Error str")

    def test_triangle_perimeter_1(self):
        res = perimeter(5, 0, 1)
        self.assertEqual(res,0)

    def test_triangle_perimeter_2(self):
        res = perimeter(1, 5, 3)
        self.assertEqual(res, 9)

    def test_triangle_perimeter_3(self):
        res = perimeter(-1, -2, -1)
        self.assertEqual(res, "Error negative value")

    def test_triangle_perimeter_4(self):
        res = perimeter("1", "1", "4")
        try:
            perimeter("1","1","4")
        except TypeError:
            print("Error str")
