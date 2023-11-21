import math
import unittest

def area(a):
    
    return a * a


def perimeter(a):
    
    return 4 * a


class TestSquareMethods(unittest.TestCase):
    
    def test_area_int(self):
        result = area(4)
        self.assertEqual(result,16)

    def test_area_real(self):
        result = area(3.5)
        self.assertEqual(result,12.25)

    def test_area_zero(self):
        result = area(0)
        self.assertEqual(result,0)

    def test_perimeter_zero(self):
        result = perimeter(0)
        self.assertEqual(result,0)

    def test_perimeter_int(self):
        result = perimeter(5)
        self.assertEqual(result,20)

    def test_perimeter_real(self):
        result = perimeter(2.5)
        self.assertEqual(result,10)
        
        
if __name__ == '__main__':
    unittest.main()
