import unittest
def area(a):
    '''
        Возвращает площадь квадрата по заданной стороне.

            Параметры:
                a (int): сторона квадрата

            Возвращаемые значения:
                area (int): площадь квадрата
        '''
    return a * a


def perimeter(a):
    '''
            Возвращает периметр квадрата по заданной стороне.

                Параметры:
                    a (int): сторона квадрата

                Возвращаемые значения:
                    area (int): периметр квадрата
            '''
    return 4 * a

class SquareTestCase (unittest.TestCase):
    def test_zero_mul_area(self):
        res = area (0)
        self.assertEqual(res, 0)

    def test_square_mul_area(self):
        res = area(10)
        self.assertEqual(res, 100)

    def test_zero_mul_perimeter(self):
        res = perimeter (0)
        self.assertEqual(res, 0)

    def test_square_mul_perimeter(self):
        res = perimeter(10)
        self.assertEqual(res, 40)