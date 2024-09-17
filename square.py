import unittest
def area(a):
    '''
        Возвращает площадь квадрата по заданной стороне.

            Параметры:
                a (int): сторона квадрата

            Возвращаемые значения:
                area (int): площадь квадрата
        '''
    if type(a) != int:
        return f"Input data must be int"
    return a * a


def perimeter(a):
    '''
            Возвращает периметр квадрата по заданной стороне.

                Параметры:
                    a (int): сторона квадрата

                Возвращаемые значения:
                    area (int): периметр квадрата
            '''
    if type(a) != int:
        return f"Input data must be int"
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


    def test_circle_str_perimeter(self):
        res = perimeter("12")
        self.assertEqual(res, "Input data must be int")

    def test_circle_str_area(self):
        res = area("8")
        self.assertEqual(res, "Input data must be int")

    def test_square_area_1(self):
        res = area(5)
        self.assertEqual(res, round(5*5, 2))

    def test_square_area_2(self):
        res = area(0)
        self.assertEqual(res, round(0, 2))

    def test_square_area_3(self):
        res = area(1)
        self.assertEqual(res, round(1, 2))

    def test_square_area_4(self):
        res = area(8)
        self.assertEqual(res, round(8*8, 2))


    def test_square_perimeter_1(self):
        res = perimeter(7)
        self.assertEqual(res, round(4 * 7, 2))

    def test_square_perimeter_2(self):
        res = perimeter(4)
        self.assertEqual(res, round(4 * 4, 2))

    def test_square_perimeter_3(self):
        res = perimeter(87)
        self.assertEqual(res, round(4 * 87, 2))

    def test_square_perimeter_4(self):
        res = perimeter(17)
        self.assertEqual(res, round(4 * 17, 2))