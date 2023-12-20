import unittest,random

from circle import *
from square import area as square_area, perimeter as square_perimeter
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter


class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertAlmostEqual(res, 0, delta=0.1)

    def test_small_numbers_area(self):
        res = area(15)
        self.assertAlmostEqual(res, 706.86, delta=0.1)

    def test_big_numbers_area(self):
        res = area(6173390)
        self.assertAlmostEqual(res, 119728433662581.97, delta=0.1)

    def test_negative(self):
        with self.assertRaises(TypeError):
            area(-9)

    def test_float_area(self):
        res = area(913.8172)
        self.assertAlmostEqual(res, 2623424.2, delta=0.1)

    def test_zero_perim(self):
        res = perimeter(0)
        self.assertAlmostEqual(res, 0, delta=0.1)

    def test_small_numbers_perim(self):
        res = perimeter(15)
        self.assertAlmostEqual(res, 94.25, delta=0.1)

    def test_big_numbers_perim(self):
        res = perimeter(6173391)
        self.assertAlmostEqual(res, 38788559.63, delta=0.1)

    def test_negative(self):
        with self.assertRaises(TypeError):
            perimeter(-9)

    def test_float_perim(self):
        res = perimeter(913.8172)
        self.assertAlmostEqual(res, 5741.6, delta=0.1)


class TestRectangle(unittest.TestCase):
    def test_zero_area(self):
        res6 = rectangle_area(10, 0)
        self.assertEqual(res6, 0)

    def test_square_area(self):
        res7 = rectangle_area(10, 10)
        self.assertEqual(res7, 100)

    def test_negative(self):
       with self.assertRaises(TypeError):
            rectangle_area(-9,0)


    def test_small_area(self):
        res8 = rectangle_area(3, 3)
        self.assertEqual(res8, 9)

    def test_large_area(self):
        res9 = rectangle_area(123456789, 987654321)
        self.assertEqual(res9, 121932631112635269)

    def test_square_perimeter(self):
        res10 = rectangle_perimeter(20, 20)
        self.assertEqual(res10, 80)
    def test_negative(self):
       with self.assertRaises(TypeError):
            rectangle_perimeter(-3,0)



    def test_large_perimeter(self):
        res11 = rectangle_perimeter(75384901072, 29813745390)
        self.assertEqual(res11, 210397292924)


class TestSquare(unittest.TestCase):
    def test_zero_area(self):
        res12 = square_area(0)
        self.assertEqual(res12, 0)
    def test_negative(self):
       with self.assertRaises(TypeError):
            square_area(-20)

    def test_small_area(self):
        res13 = square_area(2.5)
        self.assertEqual(res13, 6.25)

    def test_large_area(self):
        res14 = square_area(10)
        self.assertEqual(res14, 100)

    def test_zero_perimeter(self):
        res15 = square_perimeter(0)
        self.assertEqual(res15, 0)

    def test_negative(self):
       with self.assertRaises(TypeError):
            square_perimeter(-53)


    def test_small_perimeter(self):
        res16 = square_perimeter(5.5)
        self.assertEqual(res16, 22)

    def test_large_perimeter(self):
        res17 = square_perimeter(15)
        self.assertEqual(res17, 60)


class TestTriangle(unittest.TestCase):
    def test_a_zero_area(self):
        res18 = triangle_area(0, 15)
        self.assertEqual(res18, 0)

    def test_negative(self):
        with self.assertRaises(TypeError):
            triangle_area(-4,0,0)

    def test_b_zero_area(self):
        res19 = triangle_area(-5, 10)
        self.assertEqual(res19, -25)

    def test_large_area(self):
        res20 = triangle_area(5879324522, 134513256136)
        self.assertEqual(res20, 395423542667225858048)

    def test_large_perimeter(self):
        res21 = triangle_perimeter(7852134593240, 481325073680324, 5329679326862463)
        self.assertEqual(res21, 5818856535136027)

    def test_negative(self):
        with self.assertRaises(ValueError):
            triangle_perimeter(-5, 0, 0)


    def test_small_perimeter(self):
        res22 = triangle_perimeter(5.5, 6, 4)
        self.assertEqual(res22, 15.5)


if __name__ == '__main__':
    unittest.main()
