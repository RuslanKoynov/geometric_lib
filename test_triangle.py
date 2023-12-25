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
         with self.assertRaises(ValueError):
            (area(-1,-2))


    def test_triangle_area_4(self):
        with self.assertRaises(TypeError):
            (area('1','3','5'))

    def test_triangle_perimeter_1(self):
        res = perimeter(5, 0, 1)
        self.assertEqual(res,0)

    def test_triangle_perimeter_2(self):
        res = perimeter(1, 5, 3)
        self.assertEqual(res, 9)

    def test_triangle_perimeter_3(self):
        with self.assertRaises(ValueError):
            (perimeter(-1,-2,-5))

    def test_triangle_perimeter_4(self):
        with self.assertRaises(TypeError):
            (perimeter('1','3','5'))