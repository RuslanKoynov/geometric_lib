import unittest

from square import area
from square import perimeter

class squareTest(unittest.TestCase):
    def test_square_area_1(self):
        res = area(5)
        self.assertEqual(res, 25)

    def test_square_area_2(self):
         with self.assertRaises(ValueError):
            (area(-5))


    def test_square_area_3(self):
        with self.assertRaises(TypeError):
            (area('5'))
    def test_square_area_4(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_square_perimeter_1(self):
        res = perimeter(5)
        self.assertEqual(res,20)

    def test_square_perimeter_2(self):
         with self.assertRaises(ValueError):
            (perimeter(-1,-2,-5))


    def test_square_perimeter_3(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_square_perimeter_4(self):
        with self.assertRaises(TypeError):
            (perimeter('5'))
