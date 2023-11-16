import math
import unittest

def area(r):
    '''Returns area of a circle with radius r'''
    return math.pi * r * r


def perimeter(r):
    '''Returns perimeter (length) of a circle with radius r'''
    return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):
    def test_area_zero_radius(self):
        res = area(0.0)
        self.assertEqual(res, 0.0)

    def test_area_redius_5(self):
        res = area(5.0)
        self.assertAlmostEqual(res, 78.5398, places=4)

    def test_perimeter_zero_radius(self):
        res = perimeter(0.0)
        self.assertEqual(res, 0.0)

    def test_area_redius_5(self):
        res = perimeter(5.0)
        self.assertAlmostEqual(res, 31.4159, places=4)
