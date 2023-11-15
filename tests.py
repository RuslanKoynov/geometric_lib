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

    def test_small_perimeter(self):
        res4 = circle_perimeter(20)
        self.assertEqual(res4, 125.66370614359172)

    def test_large_perimeter(self):
        res5 = circle_perimeter(75384901072)
        self.assertEqual(res5, 473657302798.77704)


class TestRectangle(unittest.TestCase):
    def test_zero_area(self):
        res1 = rectangle_area(10, 0)
        self.assertEqual(res1, 0)

    def test_square_area(self):
        res2 = rectangle_area(10, 10)
        self.assertEqual(res2, 100)

    def test_small_area(self):
        res3 = rectangle_area(1, 1)
        self.assertEqual(res3, 1)

    def test_large_area(self):
        res4 = rectangle_area(123456789, 987654321)
        self.assertEqual(res4, 121932631112635269)

    def test_square_perimeter(self):
        res5 = rectangle_perimeter(20, 20)
        self.assertEqual(res5, 80)

    def test_large_perimeter(self):
        res6 = rectangle_perimeter(75384901072, 29813745390)
        self.assertEqual(res6, 210397292924)


class TestSquare(unittest.TestCase):
    def test_zero_area(self):
        res1 = square_area(0)
        self.assertEqual(res1, 0)

    def test_small_area(self):
        res2 = square_area(1)
        self.assertEqual(res2, 1)

    def test_large_area(self):
        res3 = square_area(10)
        self.assertEqual(res3, 100)

    def test_zero_perimeter(self):
        res4 = square_perimeter(0)
        self.assertEqual(res4, 0)

    def test_small_perimeter(self):
        res5 = square_perimeter(2)
        self.assertEqual(res5, 8)

    def test_large_perimeter(self):
        res6 = square_perimeter(15)
        self.assertEqual(res6, 60)


class TestTriangle(unittest.TestCase):
    def test_a_zero_area(self):
        res1 = triangle_area(0, 10)
        self.assertEqual(res1, 0)

    def test_b_zero_area(self):
        res2 = triangle_area(10, 0)
        self.assertEqual(res2, 0)

    def test_large_area(self):
        res3 = triangle_area(5879324522, 134513256136)
        self.assertEqual(res3, 395423542667225858048)

    def test_large_perimeter(self):
        res4 = triangle_perimeter(7852134593240, 481325073680324, 5329679326862463)
        self.assertEqual(res4, 5818856535136027)

    def test_small_perimeter(self):
        res5 = triangle_perimeter(1, 0, 34)
        self.assertEqual(res5, 35)


if __name__ == '__main__':
    unittest.main()
