import math
import unittest
class AreaTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(4), math.pi * 4 * 4)
        self.assertEqual(area(0), 0)
        self.assertEqual(area(1), math.pi)
    def test_values(self):
        self.assertRaises(ValueError, area, -2)
        self.assertRaises(ValueError, area, -1)
    def test_types(self):
        self.assertRaises(TypeError, area, 'one')
        self.assertRaises(TypeError, area, [1, 2])
class PerimetrTestCase(unittest.TestCase):
    def test_perimeter(self):
        self.assertEqual(perimeter(3), 2 * math.pi * 3)
        self.assertEqual(perimeter(0), 0)
        self.assertEqual(perimeter(1), 2 * math.pi)
    def test_values(self):
        self.assertRaises(ValueError, perimeter, -2)
        self.assertRaises(ValueError, perimeter, -1)
    def test_types(self):
        self.assertRaises(TypeError, perimeter, 'one')
        self.assertRaises(TypeError, perimeter, [1, 2])
def area(r):
    if type(r) not in [int, float]:
        raise TypeError("radius must be a number only")
    if r < 0:
        raise ValueError("radius can't be negative")
    return math.pi * r * r
def perimeter(r):
    if type(r) not in [int, float]:
        raise TypeError("radius must be a number only")
    if r < 0:
        raise ValueError("radius can not be negative")
    return 2 * math.pi * r
if __name__ == '__main__':
    unittest.main()
    
