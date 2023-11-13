import unittest, random
from circle import *

class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertAlmostEqual(res, 0, delta=0.1)

    def test_small_numbers_area(self):
        res = area(15)
        self.assertAlmostEqual(res, 706.86, delta=0.1)

    def test_big_numbers_area(self):
        res = area(6173390)
        self.assertAlmostEqual(res, 119728433662581.97, delta=0.1)

    def test_small_random_number_area(self):
        a = random.randint(1, 20)
        res = area(a)
        self.assertAlmostEqual(res, math.pi*a**2, delta=0.1)

    def test_big_random_number_area(self):
        a = random.randint(1000, 10000000)
        res = area(a)
        self.assertAlmostEqual(res, math.pi*a**2, delta=0.1)

    def test_string_area(self):
        res = area('0')
        self.assertEqual(res, TypeError)

    def test_float_area(self):
        res = area(913.8172)
        self.assertAlmostEqual(res, 2623424.251842681, delta=0.1)

    def test_zero_perim(self):
        res = perimeter(0)
        self.assertAlmostEqual(res, 0, delta=0.1)

    def test_small_numbers_perim(self):
        res = perimeter(15)
        self.assertAlmostEqual(res, 94.25, delta=0.1)

    def test_big_numbers_perim(self):
        res = perimeter(6173391)
        self.assertAlmostEqual(res, 38788559.63, delta=0.1)

    def test_small_random_number_perim(self):
        a = random.randint(1, 20)
        res = perimeter(a)
        self.assertAlmostEqual(res, 2*math.pi*a, delta=0.1)

    def test_big_random_number_perim(self):
        a = random.randint(1000, 10000000)
        res = perimeter(a)
        self.assertAlmostEqual(res, 2*math.pi*a, delta=0.1)
    
    def test_string_perim(self):
        res = perimeter('0')
        self.assertEqual(res, TypeError)
    
    def test_float_perim(self):
        res = perimeter(913.8172)
        self.assertAlmostEqual(res, 5741.682804487989, delta=0.1)