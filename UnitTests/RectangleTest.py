import random, unittest
from rectangle import *

class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_square_area(self):
        res = area(10, 10)
        self.assertEqual(res, 100)
        
    def test_small_numbers_area(self):
        res = area(1, 15)
        self.assertEqual(res, 15)

    def test_big_numbers_area(self):
        res = area(6173391, 1572631732)
        self.assertEqual(res, 9708470580643212)

    def test_small_random_number_area(self):
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        res = area(a, b)
        self.assertEqual(res, a * b)

    def test_big_random_number_area(self):
        a = random.randint(1000, 10000000)
        b = random.randint(1000, 10000000)
        res = area(a, b)
        self.assertEqual(res, a * b)

    def test_string_area(self):
        res = area('0', '10')
        self.assertEqual(res, TypeError)

    def test_float_area(self):
        res = area(913.8172, 1723.71238)
        self.assertAlmostEqual(res, 1575158.020696936, delta=0.1)
    
    def test_zero_perim(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_same_numbers_perim(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_small_numbers_perim(self):
        res = perimeter(1, 15)
        self.assertEqual(res, 32)

    def test_big_numbers_perim(self):
        res = perimeter(6173391, 1572631732)
        self.assertEqual(res, 3157610246)

    def test_small_random_number_perim(self):
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        res = perimeter(a, b)
        self.assertEqual(res, 2 * (a + b))

    def test_big_random_number_perim(self):
        a = random.randint(1000, 10000000)
        b = random.randint(1000, 10000000)
        res = perimeter(a, b)
        self.assertEqual(res, 2 * (a + b))
    
    def test_string_perim(self):
        res = area('0', '10')
        self.assertEqual(res, TypeError)

    def test_float_perim(self):
        res = perimeter(913.8172, 1723.71238)
        self.assertAlmostEqual(res, 5275.05916, delta=0.1)