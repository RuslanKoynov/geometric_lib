import unittest

from circle import area as circle_area, perimeter as circle_perimeter
from square import area as square_area, perimeter as square_perimeter
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter


class TestCircle(unittest.TestCase):
    def test_zero_area(self):
        res1 = circle_area(0)
        self.assertEqual(res1, 0)
    def test_small_area(self):
        res2 = circle_area(1)
        self.assertEqual(res2, 3.141592653589793)

    def test_large_area(self):
        res3 = circle_area(10)
        self.assertEqual(res3, 314.1592653589793)

    def test_negative_per(self):
        res4 = circle_area("-10")
        self.assertRaises(res4,TypeError)

    def test_small_perimeter(self):
        res5 = circle_perimeter(20)
        self.assertEqual(res5, 125.66370614359172)

    def test_large_perimeter(self):
        res6 = circle_perimeter(75384901072)
        self.assertEqual(res6, 473657302798.77704)
    def test_negative_per(self):
        res7 = circle_perimeter("-10")
        self.assertRaises(res7,TypeError)

class TestRectangle(unittest.TestCase):
    def test_zero_area(self):
        res8 = rectangle_area(10, 0)
        self.assertEqual(res8, 0)

    def test_square_area(self):
        res9 = rectangle_area(10, 10)
        self.assertEqual(res9, 100)

    def test_small_area(self):
        res10 = rectangle_area(1, 1)
        self.assertEqual(res10, 1)

    def test_large_area(self):
        res11 = rectangle_area(123456789, 987654321)
        self.assertEqual(res11, 121932631112635269)

    def test_negative_per(self):
        res12 = rectangle_area("-10","-10")
        self.assertRaises(res12,TypeError)
    def test_square_perimeter(self):
        res13 = rectangle_perimeter(20, 20)
        self.assertEqual(res13, 80)

    def test_large_perimeter(self):
        res14 = rectangle_perimeter(75384901072, 29813745390)
        self.assertEqual(res14, 210397292924)

    def test_negative_per(self):
        res15 = rectangle_perimeter("-10","-10")
        self.assertRaises(res15,TypeError)

class TestSquare(unittest.TestCase):
    def test_zero_area(self):
        res16 = square_area(0)
        self.assertEqual(res16, 0)

    def test_small_area(self):
        res17 = square_area(1)
        self.assertEqual(res17, 1)

    def test_large_area(self):
        res18 = square_area(10)
        self.assertEqual(res18, 100)

    def test_negative_per(self):
        res19 = square_area("-10")
        self.assertRaises(res19,TypeError)

    def test_zero_perimeter(self):
        res20 = square_perimeter(0)
        self.assertEqual(res20, 0)

    def test_small_perimeter(self):
        res21 = square_perimeter(2)
        self.assertEqual(res21, 8)

    def test_large_perimeter(self):
        res22 = square_perimeter(15)
        self.assertEqual(res22, 60)

    def test_negative_per(self):
        res23 = square_perimeter("-10")
        self.assertRaises(res23,TypeError)


class TestTriangle(unittest.TestCase):
    def test_a_zero_area(self):
        res24 = triangle_area(0, 15)
        self.assertEqual(res24, 0)

    def test_b_zero_area(self):
        res25 = triangle_area(15, 0)
        self.assertEqual(res25, 0)

    def test_large_area(self):
        res26 = triangle_area(5879324522, 134513256136)
        self.assertEqual(res26, 395423542667225858048)

    def test_negative_per(self):
        res27 = triangle_area("-10")
        self.assertRaises(res27,TypeError)

    def test_large_perimeter(self):
        res28 = triangle_perimeter(7852134593240, 481325073680324, 5329679326862463)
        self.assertEqual(res28, 5818856535136027)

    def test_small_perimeter(self):
        res29 = triangle_perimeter(1, 0, 34)
        self.assertEqual(res29, 35)
    def test_negative_per(self):
        res30 = triangle_perimeter("-10")
        self.assertRaises(res30,TypeError)


if __name__ == '__main__':
    unittest.main()

