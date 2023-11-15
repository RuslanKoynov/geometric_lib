import unittest
class AreaTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(4), 4 * 4)
        self.assertEqual(area(0), 0)
    def test_values(self):
        self.assertRaises(ValueError, area, -4)
        self.assertRaises(ValueError, area, -1)
    def test_types(self):
        self.assertRaises(TypeError, area, 'three')
        self.assertRaises(TypeError, area, [1, 2])
class PerimetrTestCase(unittest.TestCase):
    def test_perimeter(self):
        self.assertEqual(perimeter(3), 4 * 3)
        self.assertEqual(perimeter(0), 0)
    def test_values(self):
        self.assertRaises(ValueError, perimeter, -3)
        self.assertRaises(ValueError, perimeter, -1)
    def test_types(self):
        self.assertRaises(TypeError, perimeter, 'four')
        self.assertRaises(TypeError, perimeter, [1, 2])
def area(a):
    if type(a) not in [int, float]:
        raise TypeError("Values must be a numbers only")
    if a < 0:
        raise ValueError("Numbers can not be negative")
    return a * a
def perimeter(a):
    if type(a) not in [int, float]:
        raise TypeError('Values must be a numbers only')
    if a < 0:
        raise ValueError('Numbers can not be negative')
    return 4 * a
if __name__ == '__main__':
    unittest.main()
