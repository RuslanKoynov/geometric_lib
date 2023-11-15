import unittest
class area_test_case(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(3, 4), 3 * 4)
        self.assertEqual(area(0, 0), 0)
    def test_values(self):
        self.assertRaises(ValueError, area, -3, 4)
        self.assertRaises(ValueError, area, -3, -4)
    def test_types(self):
        self.assertRaises(TypeError, area, 'three', 4)
        self.assertRaises(TypeError, area, 'xyz', 'abc')
        self.assertRaises(TypeError, area, [1, 2], [3, 4])

class perimeter_test_case(unittest.TestCase):
    def test_perimeter(self):
        self.assertEqual(perimeter(3, 4), (3 + 4) * 2)
        self.assertEqual(perimeter(0, 0), 0)
    def test_values(self):
        self.assertRaises(ValueError, area, -3, 4)
        self.assertRaises(ValueError, area, -3, -4)
    def test_types(self):
        self.assertRaises(TypeError, area, 'three', 4)
        self.assertRaises(TypeError, area, 'xyz', 'abc')
        self.assertRaises(TypeError, area, [1, 2], [3, 4])

def area(a, b):
    if a < 0 or b < 0:
        raise ValueError("numbers can't be negative")
    if not(type(a) in [int, float]) or not(type(b) in [int, float]):
        raise TypeError('input values must be a numbers only')
    return a * b

def perimeter(a, b):
    if not(type(a) in [int, float] or not(type(b) in [int, float])):
        if a < 0 or b < 0:
            raise ValueError("numbers can't be negative")
    if type(a) not in [int, float] or type(b) not in [int, float]:
        raise TypeError('input values must be a numbers only')
    return (a + b) * 2
