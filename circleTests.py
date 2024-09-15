import unittest
from circle import area
from circle import perimeter


class CircleTests(unittest.TestCase):

    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_one_area(self):
        res = area(1)
        self.assertEqual(res, 3.141592653589793)

    def test_float_area(self):
        res = area(2.5)
        self.assertEqual(res, 19.634954084936208)

    def test_negative_area(self):
        res = area(-5)
        self.assertEqual(res, 78.53981633974483)

    def test_string_area(self):
        res = area("123")
        self.assertEqual(res, 47529.15525615998)


    def test_zero_perimeter(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_one_perimeter(self):
        res = perimeter(1)
        self.assertEqual(res, 6.283185307179586)

    def test_float_perimeter(self):
        res = perimeter(2.5)
        self.assertEqual(res, 15.707963267948966)

    def test_negative_perimeter(self):
        res = perimeter(-5)
        self.assertEqual(res, -31.41592653589793)

    def test_string_perimeter(self):
        res = perimeter("123")
        self.assertEqual(res, 772.8317927830891)