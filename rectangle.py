import unittest

def area(a, b):
    '''Returns area of a rectangle with a and b sides'''
    return a * b;

def perimeter(a, b):
    '''Returns perimeter of a rectangle with a and b sides'''
    return 2 * (a + b);

class RectangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        result = area(7, 0);
        self.assertEqual(result, 0);

    def test_area_1_2(self):
        result = area(1, 2);
        self.assertEqual(result, 2);

    def test_perimeter_zero(self):
        result = perimeter(7, 0);
        self.assertEqual(result, 7);

    def test_perimeter(self):
        result = perimeter(1, 2);
        self.assertEqual(result, 6);
