import unittest
import math

def area(r):
    if r < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * r * r

def perimeter(r):
    if r < 0:
        raise ValueError("Radius cannot be negative")
    return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):
    def test_area_1(self):
        res = area(0)
        self.assertAlmostEqual(res, 0, delta=0.1)

    def test_perimeter_1(self):
        res = perimeter(0)
        self.assertAlmostEqual(res, 0, delta=0.1)

    def test_area_2(self):
        res = area(5)
        self.assertAlmostEqual(res, 78.5, delta=0.1)

    def test_perimeter_2(self):
        res = perimeter(5)
        self.assertAlmostEqual(res, 31.4, delta=0.1)

    def test_area_negative(self):
        try:
            area(-5)
        except ValueError:
            self.fail("Unexpected ValueError")

    def test_perimeter_negative(self):
        try:
            perimeter(-5)
        except ValueError:
            self.fail("Unexpected ValueError")
