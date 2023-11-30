from rectangle import area
from rectangle import perimeter

import unittest

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
       res = area(10, 0)
       self.assertEqual(res, 0)
       
    def test_square_mul(self):
       res = area(10, 10)
       self.assertEqual(res, 100)

    def test_small_mul(self):
        res = area(1, 15)
        self.assertEqual(res, 15)

    def test_big_mul(self):
        res = area(5465467, 6584567)
        self.assertEqual(res, 35987733647789)

    def test_string_mul(self):
        self.assertRaises(TypeError, area, '0', '10')

    def test_float_mul(self):
        res = area(456.23, 986.4567)
        self.assertEqual(res, 450051.140241)

    def test_negative_mul(self):
        self.assertRaises(TypeError, area, -10, 1)

    def test_zero_per(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_the_same_per(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_small_per(self):
        res = perimeter(1, 15)
        self.assertEqual(res, 32)

    def test_big_per(self):
        res = perimeter(5465467, 6584567)
        self.assertEqual(res, 24100068)

    def test_string_per(self):
        self.assertRaises(TypeError, area, '0', '10')

    def test_float_per(self):
        res = perimeter(456.23, 986.4567)
        self.assertEqual(res, 2885.3734)

    def test_negative_per(self):
        self.assertRaises(TypeError, perimeter, -10, 1)