from square import area
from square import perimeter

import unittest

class SquareTestCase(unittest.TestCase):
    def test_zero_mul(self):
       res = area(0)
       self.assertEqual(res, 0)
       
    def test_square_mul(self):
       res = area(10)
       self.assertEqual(res, 100)

    def test_small_mul(self):
        res = area(15)
        self.assertEqual(res, 225)

    def test_big_mul(self):
        res = area(6584567)
        self.assertEqual(res, 43356522577489)

    def test_string_mul(self):
        self.assertRaises(TypeError, area, '10')

    def test_float_mul(self):
        res = area(986.4567)
        self.assertEqual(res, 973096.8209748899)

    def test_negative_mul(self):
        self.assertRaises(TypeError, area, -10)  

    def test_zero_per(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_small_per(self):
        res = perimeter(15)
        self.assertEqual(res, 60)

    def test_big_per(self):
        res = perimeter(5465467)
        self.assertEqual(res, 21861868)

    def test_string_per(self):
        self.assertRaises(TypeError, area, '10')

    def test_float_per(self):
        res = perimeter(456.23)
        self.assertEqual(res, 1824.92)

    def test_negative_per(self):
        self.assertRaises(TypeError, perimeter, -10)