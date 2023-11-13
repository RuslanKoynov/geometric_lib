import unittest, random
from triangle import *

class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0, 0)
        self.assertEqual(res, 0)

    def test_small_numbers_area(self):
        res = area(15, 2)
        self.assertEqual(res, 15)

    def test_big_numbers_area(self):
        res = area(6173391, 126381732)
        self.assertEqual(res, 390101923446606)

    def test_small_random_number_area(self):
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        res = area(a, b)
        self.assertEqual(res, a*b/2)

    def test_big_random_number_area(self):
        a = random.randint(1000, 10000000)
        b = random.randint(1000, 10000000)
        res = area(a, b)
        self.assertEqual(res, a*b/2)

    def test_string_area(self):
        res = area('0', '91')
        self.assertEqual(res, TypeError)

    def test_float_area(self):
        res = area(913.8172, 1273.671)
        self.assertAlmostEqual(res, 581951.2334706, delta=0.1)

    def test_zero_perim(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_small_numbers_perim(self):
        res = perimeter(15, 10, 5)
        self.assertEqual(res, 30)

    def test_big_numbers_perim(self):
        res = perimeter(6173391, 126371832, 981331)
        self.assertEqual(res, 133526554)

    def test_small_random_number_perim(self):
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        c = random.randint(1, 20)
        res = perimeter(a, b, c)
        self.assertEqual(res, a + b + c)

    def test_big_random_number_perim(self):
        a = random.randint(1000, 10000000)
        b = random.randint(1000, 10000000)
        c = random.randint(1000, 10000000)
        res = perimeter(a, b, c)
        self.assertEqual(res, a + b + c)
    
    def test_string_perim(self):
        res = perimeter('0', '10', '15')
        self.assertEqual(res, TypeError)
    
    def test_float_perim(self):
        res = perimeter(913.8172, 1832.9123, 89123.6417)
        self.assertAlmostEqual(res, 91870.3712, delta=0.1)