from circle import area
from circle import perimeter

import unittest

class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
       res = area(0)
       self.assertEqual(res, 0)
       
    def test_square_mul(self):
       res = area(10)
       self.assertEqual(res, 314.1592653589793)

    def test_small_mul(self):
        res = area(15)
        self.assertEqual(res, 706.8583470577034)

    def test_big_mul(self):
        res = area(6173391)
        self.assertEqual(res, 119728472451138.44)

    def test_string_mul(self):
        self.assertRaises(TypeError, area, '10')

    def test_float_mul(self):
        res = area(456.23)
        self.assertEqual(res, 653909.3566821157)

    def test_negative_mul(self):
        self.assertRaises(TypeError, area, -10)     

    def test_zero_per(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_the_same_per(self):
        res = perimeter(10)
        self.assertEqual(res, 62.83185307179586)

    def test_small_per(self):
        res = perimeter(15)
        self.assertEqual(res, 94.24777960769379)

    def test_big_per(self):
        res = perimeter(6173391)
        self.assertEqual(res, 38788559.62667469)

    def test_string_per(self):
        self.assertRaises(TypeError, area, '10')

    def test_float_per(self):
        res = perimeter(456.23)
        self.assertEqual(res, 2866.577632694543)

    def test_negative_per(self):
        self.assertRaises(TypeError, perimeter, -10)