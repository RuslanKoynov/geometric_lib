import unittest
import circle

class CircleTestCase(unittest.TestCase):
    def test_positive_area(self):
        res = circle.area(10)
        self.assertAlmostEqual(res, 314.1592653589793)

    def test_zero_area(self):
        res = circle.area(0)
        self.assertAlmostEqual(res, 0)

    def test_negative_area(self):
        res = circle.perimeter(-10)
        self.assertAlmostEqual(res,'The radius cannot be negative')

    def test_positive_perimeter(self):
        res = circle.perimeter(10)
        self.assertAlmostEqual(res, 62.83185307179586)

    def test_zero_perimeter(self):
        res = circle.perimeter(0)
        self.assertAlmostEqual(res, 0)

    def test_negative_perimetr(self):
        res = circle.perimeter(-10)
        self.assertAlmostEqual(res,'The radius cannot be negative')