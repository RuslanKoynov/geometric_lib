import math
import unittest

def area(r):
    return math.pi * r * r


def perimeter(r):
    return 2 * math.pi * r


class TestCircleMethods(unittest.TestCase):
    
    def test_area_int(self):
        result = area(5)
        self.assertAlmostEqual(result,78.54,delta=0.1)

    def test_area_real(self):
        result = area(3.5)
        self.assertAlmostEqual(result,38.48,delta=0.1)

    def test_area_zero(self):
        result = area(0)
        self.assertEqual(result,0)

    def test_area_negative(self):
       with self.assertRaises(Exception):
            area(-7)

    def test_perimeter_zero(self):
        result = perimeter(0)
        self.assertEqual(result,0)

    def test_perimeter_int(self):
        result = perimeter(5)
        self.assertAlmostEqual(result,31.42,delta=0.1)

    def test_perimeter_real(self):
        result = perimeter(3.5)
        self.assertAlmostEqual(result,21.99,delta=0.1)

    def test_perimeter_negative(self):
        with self.assertRaises(Exception):
            perimeter(-2)
        
        
if __name__ == '__main__':
    unittest.main()
