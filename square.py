import unittest
class SquareTestCase(unittest.TestCase):
    def area_test_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def area_test_number(self):
        res = area(9)
        self.assertEqual(res,81)

    def area_test_float_number(self):
        res = area(3.123)
        self.assertEqual(res,9.753129000000001)

    def perimeter_test_zero(self):
        res = perimeter(0)
        self.assertEqual(res,0)

    def perimeter_test_number(self):
        res = perimeter(13)
        self.assertEqual(res,52)

    def perimeter_test_float_number(self):
        res = perimeter(4.1675)
        self.assertEqual(res,16.67)


def area(a):
    '''
        Возвращает площадь квадрата со стороной а.

            Параметры:
                а(int): сторона квадрата

            Возвращаемое значение:
                 a*a(int): площадь квадрата
        '''
    return a * a


def perimeter(a):
    '''
        Возвращает периметр квадрата со стороной a.

            Параметры:
                a(int): сторона квадрата.

            Возвращаемое значение:
                4*а(int): периметр квадрата.
        '''
    return 4 * a

print(perimeter(4.1675))