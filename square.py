import unittest
class SquareTestCase(unittest.TestCase):
    def test_area_test_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_test_number(self):
        res = area(9)
        self.assertEqual(res,81)

    def test_area_test_float_number(self):
        res = area(3.123)
        self.assertAlmostEqual(res,9.75,places=2)

    def test_perimeter_test_zero(self):
        res = perimeter(0)
        self.assertEqual(res,0)

    def test_perimeter_test_number(self):
        res = perimeter(13)
        self.assertEqual(res,52)

    def test_perimeter_test_float_number(self):
        res = perimeter(4.1675)
        self.assertAlmostEqual(res,16.67,places=2)

    def test_area_test_negative_number(self):
        with self.assertRaises(Exception):
            area(-1)

    def test_perimeter_test_negative_number(self):
        with self.assertRaises(Exception):
            perimeter(-1)


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
