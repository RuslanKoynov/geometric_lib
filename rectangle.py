import math
import unittest

def area(a, b):
  
    return a * b 

def perimeter(a, b):
  
    return (a + b)*2

class TestRectangleMethods(unittest.TestCase):
    
    def test_area_int(self):
        result = area(5,6)
        self.assertEqual(result,30)

    def test_area_real(self):
        result = area(3.5,5.5)
        self.assertEqual(result,19.25)

    def test_area_zero(self):
        result = area(0,0)
        self.assertEqual(result,0)

    def test_area_negative(self):
        result = area(2,-2)
        self.assertEqual(result, "Error")

    def test_perimeter_zero(self):
        result = perimeter(0,0)
        self.assertEqual(result,0)

    def test_perimeter_int(self):
        result = perimeter(5,2)
        self.assertEqual(result,14)

    def test_perimeter_real(self):
        result = perimeter(3.5,2.5)
        self.assertEqual(result,12.0)
        
        
if __name__ == '__main__':
    unittest.main()


