import unittest

def area(a, h):
    '''Returns area of a triangle where b is the length of the base of the triangle, and h is the height'''
    return a * h / 2;

def perimeter(a, b, c):
    '''Returns perimeter of a triangle with sides a, b, and c'''
    return a + b + c;

class TriangleTestCase(unittest.TestCase):
    def test_area_zero_height(self):
        result = area(7, 0);
        self.assertEqual(result, 0);

    def test_area(self):
        result = area(5, 6);
        self.assertEqual(result, 15);

    def test_area_negative_value(self):
        with self.assertRaises(ValueError):
            result = area(-6, -5);

    def test_perimeter_3_4_5(self):
        result = perimeter(3, 4, 5);
        self.assertEqual(result, 12);

    def test_perimeter_zero_side(self):
        result = perimeter(3, 0, 3);
        self.assertEqual(result, 3);

    def test_perimeter_negative_value(self):
        with self.assertRaises(ValueError):
            result = perimeter(-6, 1, 2);
