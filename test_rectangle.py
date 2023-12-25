import unittest


from rectangle import area
from rectangle import perimeter

class RectangleTest(unittest.TestCase):
    def test_rectangle_area_1(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_rectangle_area_2(self):
        res = area(5, 5)
        self.assertEqual(res, 25)

    def test_rectangle_area_3(self):
         with self.assertRaises(ValueError):
            (area(-5,-5))


    def test_rectangle_area_4(self):
        with self.assertRaises(TypeError):
            (area('5','5'))

    def test_rectangle_perimeter_1(self):
        res = perimeter(5, 0)
        self.assertEqual(res,0)

    def test_rectangle_perimeter_2(self):
        res = perimeter(1, 5)
        self.assertEqual(res, 12)

    def test_rectangle_perimeter_3(self):
         with self.assertRaises(ValueError):
            (perimeter(-1,-5))


    def test_rectangle_perimeter_4(self):
        with self.assertRaises(TypeError):
            (perimeter('1','5'))