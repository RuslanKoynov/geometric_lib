import unittest
import math


def area(r):
    '''
    Принимает число r(радиус круга),возвращает площадь круга с этим радиусом
    '''
    return math.pi * r * r

def perimeter(r):
    '''
    Принимает число r(радиус круга),возвращает периметр круга с этим радиусом
    '''
    return 2 * math.pi * r


class CircleTest(unittest.TestCase):

    def test_area1(self):
        res = area(5)
        self.assertEqual(res, 78.5)

    def test_perimeter1(self):
        res = perimeter(5)
        self.assertEqual(res, 31.4)

    def test_area2(self):
        res = area(4.5)
        self.assertEqual(res, 63.585)

    def test_perimeter2(self):
        res = perimeter(4.5)
        self.assertEqual(res, 28.26)

    def test_area3(self):
        with self.assertRaises(Exception):
            area(-1,-20)

    def test_perimeter3(self):
        with self.assertRaises(Exception):
            perimeter(-3,-60)


if __name__ == "__main__":
    unittest.ma
