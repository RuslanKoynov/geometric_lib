from triangle import area
from triangle import perimeter

import unittest

class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
       res = area(10, 0)
       self.assertEqual(res, 0)
       
    def test_square_mul(self):
       res = area(10, 10)
       self.assertEqual(res, 50)

    def test_small_mul(self):
        res = area(1, 20)
        self.assertEqual(res, 10)

    def test_big_mul(self):
        res = area(456876, 389845)
        self.assertEqual(res, 89055412110)

    def test_string_mul(self):
        self.assertRaises(TypeError, area, '0', '10')

    def test_float_mul(self):
        res = area(567.80, 345.68)
        self.assertEqual(res, 98138.552)

    def test_negative_mul(self):
        self.assertRaises(TypeError, area, -10, 1)    

    def test_zero_per(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_the_same_per(self):
        res = perimeter(10, 10, 10)
        self.assertEqual(res, 30)

    def test_small_per(self):
        res = perimeter(1, 15, 20)
        self.assertEqual(res, 36)

    def test_big_per(self):
        res = perimeter(5465467, 6584567, 34567)
        self.assertEqual(res, 12084601)

    def test_string_per(self):
        self.assertRaises(TypeError, area, '0', '10', '1')

    def test_float_per(self):
        res = perimeter(456.23, 986.4567, 56.9)
        self.assertEqual(res, 1499.5867)

    def test_negative_per(self):
        self.assertRaises(TypeError, perimeter, -10, 1, 1)