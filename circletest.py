import unittest
import circle
class TestCircle(unittest.TestCase):
    def test_positive_area(self):
        res = circle.area(5)
        self.assertAlmostEqual(res, 78.53981633974483)

    def test_zero_area(self):
        res = circle.area(0)
        self.assertAlmostEqual(res, 0)
        
    def test_negative_area(self):
        res = circle.perimeter(-10)
        self.assertAlmostEqual(res,0)

    def test_positive_perimeter(self):
        res = circle.perimeter(5)
        self.assertAlmostEqual(res, 31.41592653589793)

    def test_zero_perimeter(self):
        res = circle.perimeter(0)
        self.assertAlmostEqual(res, 0)

    def test_negative_perimetr(self):
        res = circle.perimeter(-10)
        self.assertAlmostEqual(res,0)
