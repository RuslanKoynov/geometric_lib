import unittest

from circle import area as circle_area, perimeter as circle_perimeter
from square import area as square_area, perimeter as square_perimeter
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter


class TestCircle(unittest.TestCase):
    def test_zero_area(self):
        res1 = circle_area(3.5)
        self.assertAlmostEqual(res1, 38.48451000647496, delta = 0.01)
    def test_negative(self):
       with self.assertRaises(TypeError):
            circle_area(-5)

    def test_small_area(self):
        res2 = circle_area(-6)
        self.assertAlmostEqual(res2, 113.09733552923255, delta = 0.01)

    def test_large_area(self):
        res3 = circle_area(11)
        self.assertAlmostEqual(res3, 380.1327110843649, delta = 0.01)

    def test_small_perimeter(self):
        res4 = circle_perimeter(2.5)
        self.assertAlmostEqual(res4,15.707963267948966, delta = 0.01)

    def test_large_perimeter(self):
        res5 = circle_perimeter(67)
        self.assertAlmostEqual(res5, 420.97341558103227, delta = 0.01)
    def test_negative(self):
        with self.assertRaises(TypeError):
            circle_perimeter(-3)



class TestRectangle(unittest.TestCase):
    def test_zero_area(self):
        res6 = rectangle_area(9, 0)
        self.assertEqual(res6, 0)

    def test_square_area(self):
        res7 = rectangle_area(8, 8)
        self.assertEqual(res7, 64)

    def test_negative(self):
       with self.assertRaises(TypeError):
            rectangle_area(-78,0)


    def test_small_area(self):
        res8 = rectangle_area(4, 4)
        self.assertEqual(res8, 16)

    def test_large_area(self):
        res9 = rectangle_area(1111, 2222)
        self.assertEqual(res9, 2468642)

    def test_square_perimeter(self):
        res10 = rectangle_perimeter(20, 20)
        self.assertEqual(res10, 80)
    def test_negative(self):
       with self.assertRaises(TypeError):
            rectangle_perimeter(-223,0)



    def test_large_perimeter(self):
        res11 = rectangle_perimeter(22222, 33333)
        self.assertEqual(res11, 111110)


class TestSquare(unittest.TestCase):
    def test_zero_area(self):
        res12 = square_area(0)
        self.assertEqual(res12, 0)
    def test_negative(self):
       with self.assertRaises(TypeError):
            square_area(-70)

    def test_small_area(self):
        res13 = square_area(1.5)
        self.assertAlmostEqual(res13, 2.25, delta = 0.01)

    def test_large_area(self):
        res14 = square_area(9)
        self.assertEqual(res14, 81)

    def test_zero_perimeter(self):
        res15 = square_perimeter(0)
        self.assertEqual(res15, 0)

    def test_negative(self):
       with self.assertRaises(TypeError):
            square_perimeter(-43)


    def test_small_perimeter(self):
        res16 = square_perimeter(5.5)
        self.assertAlmostEqual(res16, 22.0, delta = 0.01)

    def test_large_perimeter(self):
        res17 = square_perimeter(20)
        self.assertEqual(res17, 80)


class TestTriangle(unittest.TestCase):
    def test_a_zero_area(self):
        res18 = triangle_area(0,11)
        self.assertEqual(res18, 0)

    def test_negative(self):
        with self.assertRaises(TypeError):
            triangle_area(-9,0,0)

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
        with self.assertRaises(TypeError):
            triangle_perimeter(-21, 0, 0)


    def test_small_perimeter(self):
        res22 = triangle_perimeter(5, 6, 7)
        self.assertEqual(res22, 18)


if __name__ == '__main__':
    unittest.main()
