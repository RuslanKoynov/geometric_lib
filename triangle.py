import math
import unittest

def area(a, h):
    
    return a * h / 2 

def perimeter(a, b, c):

    return a + b + c

class TestTriangleMethods(unittest.TestCase):
    
    def test_area_int(self):
        result = area(4,5)
        self.assertEqual(result,10)

    def test_area_real(self):
        result = area(3.5,3.75)
        self.assertAlmostEqual(result,6.56,delta=0.1)

    def test_area_zero(self):
        result = area(0,5)
        self.assertEqual(result,0)

    def test_area_negative(self):
        with self.assertRaises(Exception):
            area(-7,2)

    def test_perimeter_zero(self):
        result = perimeter(0,0,0)
        self.assertEqual(result,0)

    def test_perimeter_int(self):
        result = perimeter(5,3,2)
        self.assertEqual(result,10)

    def test_perimeter_real(self):
        result = perimeter(2.5,3.5,5.5)
        self.assertEqual(result,11.5)

    def test_perimeter_negative(self):
        with self.assertRaises(Exception):
            perimeter(-7,4,-2)
        
if __name__ == '__main__':
    unittest.main()
