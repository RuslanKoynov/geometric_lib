import unittest
class AreaTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(4, 3), (4 * 3) / 2)
        self.assertEqual(area(0, 0), 0)

    def test_values(self):
        self.assertRaises(ValueError, area, -2, 2)

    def test_types(self):
        self.assertRaises(TypeError, area, 'three', 4)
        self.assertRaises(TypeError, area, 'four', 'three')
        self.assertRaises(TypeError, area, [2], [4])

class PerimetrTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(perimeter(3, 1, 2), 3 + 1 + 2)
        self.assertEqual(perimeter(0, 0, 0), 0)

    def test_values(self):
        self.assertRaises(ValueError, perimeter, -2, 2, -1)

    def test_types(self):
        self.assertRaises(TypeError, perimeter, 'three', 2, [1])
        self.assertRaises(TypeError, perimeter, 'xyz', 'abc', 23)
        self.assertRaises(TypeError, perimeter, [4], [3], 'abc')
def area(a, h):
    if type(a) not in [int, float] or type(h) not in [int, float]:
        raise TypeError("Values must be a numbers only")
    if a < 0 or h < 0:
        raise ValueError("Numbers can't be negative")
    return a * h / 2

def perimeter(a, b, c):
    if not(type(a) in [int, float]) or not(type(b) in [int, float]) or not(type(c) in [int, float]):
        raise TypeError('Values must be a numbers only')
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Numbers can't be negative")
    return a + b + c
