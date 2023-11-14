import unittest
def area(a, h): 
    return a * h / 2
def perimeter(a, b, c): 
    return a + b + c
class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(8, 0)
        self.assertEqual(res, 0)

    def test_triangle_mul(self):
        res = area(8, 12)
        self.assertEqual(res, 48)

    def test_zero_per(self):
        res = perimeter(8, 0, 12)
        self.assertEqual(res, 20)

    def test_triangle_per(self):
        res = perimeter(6, 4, 3)
        self.assertEqual(res, 13)