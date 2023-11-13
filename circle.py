import math
import unittest

def area(r):
    """
    Принимает радиус круга, возвращает его площадь
    Входные данные: 7
    Выходные данные: 78.53981633974483
    """
    return math.pi * r * r


def perimeter(r):
    """
        Принимает радиус окружности, возвращает ее длину
        Входные данные: 5
        Выходные данные: 31.41592653589793
    """
    return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_num(self):
        res = area(10)
        self.assertEqual(res, 314.159265358979)

    def test_area_str_arg(self):
        res = area("10")
        self.assertEqual(res, "Unsupportable type string. Use numeric values.")

    def test_area_arr_arg(self):
        res = area([10])
        self.assertEqual(res, "Unsupportable type array. Use numeric values.")

    def test_area_neg_arg(self):
        res = area(-10)
        self.assertEqual(res, "Incorrect value for rectangle side length. Use not negative numbers.")

    def test_area_big_num(self):
        res = area(2147483647)
        self.assertEqual(res, 14488038902661200000)

    def test_area_float_num_1(self):
        res = area(10.0)
        self.assertEqual(res, 314.159265358979)

    def test_area_float_num_2(self):
        res = area(0.000000001)
        self.assertEqual(res, 0.00000000000000000314159265358979)

    def test_area_big_float_num(self):
        res = area(0.00000000000000000001)
        self.assertEqual(res, 3.14159265358979*10**(-40))

    def test_perimeter_zero(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_num(self):
        res = perimeter(10)
        self.assertEqual(res, 62.8318530717958)

    def test_perimeter_str_arg(self):
        res = perimeter("10")
        self.assertEqual(res, "Unsupportable type string. Use numeric values.")

    def test_perimeter_arr_arg(self):
        res = perimeter([10])
        self.assertEqual(res, "Unsupportable type array. Use numeric values.")

    def test_perimeter_neg_arg(self):
        res = perimeter(-10)
        self.assertEqual(res, "Incorrect value for rectangle side length. Use not negative numbers.")

    def test_perimeter_big_num(self):
        res = perimeter(2147483647)
        self.assertEqual(res, 13493037698.238)

    def test_perimeter_float_num(self):
        res = perimeter(10.0)
        self.assertEqual(res, 62.8318530717958)

    def test_perimeter_big_float_num(self):
        res = perimeter(0.00000000000000000001)
        self.assertEqual(res, 0.000000000000000000062831853072)

    def test_perimeter_float_num(self):
        res = perimeter(0.000000001)
        self.assertEqual(res, 0.00000000628318530717958)
