import unittest

from circle import area
from circle import perimeter


class circleTest(unittest.TestCase):
    def test_circle_area_1(self):
        self.assertAlmostEqual(area(3),28.26, delta=0.01)

    def test_circle_area_2(self):
         with self.assertRaises(ValueError):
            (area(-3))



    def test_circle_area_3(self):
        with self.assertRaises(TypeError):
            (area('3'))

    def test_circle_area_4(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_circle_perimeter_1(self):
        def test_int(self):
            self.assertAlmostEqual(perimeter(3),18.84, delta=0.01)

    def test_circle_perimeter_2(self):
         with self.assertRaises(ValueError):
            (perimeter(-3))



    def test_circle_perimeter_3(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_circle_perimeter_4(self):
        with self.assertRaises(TypeError):
            (perimeter('3'))
