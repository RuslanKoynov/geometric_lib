import unittest

def area(a):
    '''
    Принимает число, которое является стороной квадрата: a
    Возваращает площадь квадрата, вычисляя ее по формуле: a^2
    '''
    return a * a


def perimeter(a):
    '''
    Принимает число, которое является стороной квадрата: a
    Возваращает периметр квадрата, вычисляя его по формуле: 4 * a
    '''
    return 4 * a

class SquareTestCase(unittest.TestCase):
    def test_area_1(self):
        res = area(1)
        self.assertEqual(res, 1)

    def test_area_2(self):
        res = area(2)
        self.assertEqual(res, 4)

    def test_perimetr_1(self):
        res = perimeter(1)
        self.assertEqual(res, 4)

    def test_perimetr_3(self):
        res = perimeter(3)
        self.assertEqual(res, 12)