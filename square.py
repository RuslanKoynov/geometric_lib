import unittest

def area(a):
    '''Returns area of a square with side a'''
    return a * a


def perimeter(a):
    '''Returns perimeter of a square with side a'''
    return 4 * a

class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
        result = area(0);
        self.assertEqual(result, 0);

    def test_area_7(self):
        result = area(7);
        self.assertEqual(result, 49);

    def test_perimeter_zero(self):
        result = perimeter(0);
        self.assertEqual(result, 0);

    def test_perimeter_1(self):
        result = perimeter(1);
        self.assertEqual(result, 4);
