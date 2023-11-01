import unittest
class SquareTestCase(unittest.TestCase):
    def test_zero_mul(self):
       res = area(0)
       self.assertEqual(res, 0)
       
    def test_area(self):
       res = area(10)
       self.assertEqual(res, 100)

    def test_perimeter(self):
       res = perimeter(7)
       self.assertEqual(res, 28)
def area(a):
    ''' Принимает длинну стороны квадрата - a, возвращает площадь квадрата со стороной а '''
    return a * a


def perimeter(a):
    ''' Принимает длинну стороны квадрата - a, возвращает периметр квадрата со стороной а '''
    return 4 * a
