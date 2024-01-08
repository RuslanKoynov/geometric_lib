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
        self.assertAlmostEqual(res, 78.5,places=1)

    def test_perimeter1(self):
        res = perimeter(5)
        self.assertAlmostEqual(res, 31.4,places=1)

    def test_area2(self):
        res = area(4.5)
        self.assertAlmostEqual(res, 63.61,places=2)

    def test_perimeter2(self):
        res = perimeter(4.5)
        self.assertAlmostEqual(res, 28.27,places=2)

    def test_area3(self):
        with self.assertRaises(Exception):
            area(-1,-20)

    def test_perimeter3(self):
        with self.assertRaises(Exception):
            perimeter(-3,-60)


if __name__ == "__main__":
    unittest.ma
