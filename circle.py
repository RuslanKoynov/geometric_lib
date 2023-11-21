import math
import unittest

def area(r):
    return math.pi * r * r


def perimeter(r):
    return 2 * math.pi * r


class TestCircleMethods(unittest.TestCase):
    
    def test_area_int(self):
        result = area(5)
        self.assertEqual(result,78.53981633974483)

    def test_area_real(self):
        result = area(3.5)
        self.assertEqual(result,38.48451000647496)

    def test_area_zero(self):
        result = area(0)
        self.assertEqual(result,0)

    def test_perimeter_zero(self):
        result = perimeter(0)
        self.assertEqual(result,0)

    def test_perimeter_int(self):
        result = perimeter(5)
        self.assertEqual(result,31.41592653589793)

    def test_perimeter_real(self):
        result = perimeter(3.5)
        self.assertEqual(result,21.991148575128552)
        
        
if __name__ == '__main__':
    unittest.main()
