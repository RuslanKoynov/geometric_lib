import unittest, random
from square import *

class SquareTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_small_numbers_area(self):
        res = area(15)
        self.assertEqual(res, 225)

    def test_big_numbers_area(self):
        res = area(6173391)
        self.assertEqual(res, 38110756438881)

    def test_small_random_number_area(self):
        a = random.randint(1, 20)
        res = area(a)
        self.assertEqual(res, a**2)

    def test_big_random_number_area(self):
        a = random.randint(1000, 10000000)
        res = area(a)
        self.assertEqual(res, a**2)

    def test_string_area(self):
        res = area('0')
        self.assertEqual(res, TypeError)

    def test_float_area(self):
        res = area(913.8172)
        self.assertAlmostEqual(res, 835061.8750158399, delta=0.1)

    def test_zero_perim(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_small_numbers_perim(self):
        res = perimeter(15)
        self.assertEqual(res, 60)

    def test_big_numbers_perim(self):
        res = perimeter(6173391)
        self.assertEqual(res, 24693564)

    def test_small_random_number_perim(self):
        a = random.randint(1, 20)
        res = perimeter(a)
        self.assertEqual(res, 4*a)

    def test_big_random_number_perim(self):
        a = random.randint(1000, 10000000)
        res = perimeter(a)
        self.assertEqual(res, 4*a)
    
    def test_string_perim(self):
        res = perimeter('0')
        self.assertEqual(res, TypeError)
    
    def test_float_perim(self):
        res = perimeter(913.8172)
        self.assertAlmostEqual(res, 3655.2688, delta=0.1)