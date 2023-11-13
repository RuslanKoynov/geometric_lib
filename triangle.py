import unittest

def area(a, h):
    """
        Принимает длину стороны треугольника и длину высоты, проведенной к этой стороне, возвращает его площадь
        Входные данные: 12 3
        Выходные данные: 18.0
    """
    return a * h / 2

def perimeter(a, b, c):
    """
        Принимает длины трех сторон треугольника, возвращает его периметр
        Входные данные: 3 4 5
        Выходные данные: 12
    """
    return a + b + c

class TriangleTestCase(unittest.TestCase):
    def test_area_zero_a(self):
        res = area(0, 10)
        self.assertEqual(res, 0)

    def test_area_zero_h(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_area_square(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    def test_area_str_arg_a(self):
        self.assertRaises(area("10", 10), Exception)

    def test_area_str_arg_h(self):
        self.assertRaises(area(10, "10"), Exception)

    def test_area_str_arg(self):
        self.assertRaises(area("10", "10"), Exception)

    def test_area_arr_arg_a(self):
        self.assertRaises(area([10], 10), Exception)

    def test_area_arr_arg_h(self):
        self.assertRaises(area(10, [10]), Exception)

    def test_area_arr_arg(self):
        self.assertRaises(area([10], [10]), Exception)

    def test_area_neg_arg_a(self):
        self.assertRaises(area(-10, 10), Exception)

    def test_area_neg_arg_h(self):
        self.assertRaises(area(10, -10), Exception)

    def test_area_neg_arg(self):
        self.assertRaises(area(-10, -10), Exception)

    def test_area_big_num_a(self):
        res = area(2147483647, 100)
        self.assertEqual(res, 107374182350)

    def test_area_big_num_h(self):
        res = area(100, 2147483647)
        self.assertEqual(res, 107374182350)

    def test_area_float_num(self):
        res = area(10.0, 12.0)
        self.assertEqual(res, 60.0)

    def test_area_big_float_num_a(self):
        res = area(0.00000000000000000001, 0.1)
        self.assertEqual(res, 0.0000000000000000000005)

    def test_area_big_float_num_h(self):
        res = area(0.1, 0.00000000000000000001)
        self.assertEqual(res, 0.0000000000000000000005)

    def test_area_float_num_a(self):
        res = area(0.000000001, 10)
        self.assertEqual(res, 0.000000005)

    def test_area_float_num_h(self):
        res = area(10, 0.000000001)
        self.assertEqual(res, 0.000000005)

    def test_perimeter_zero_a(self):
        res = perimeter(0, 10, 10)
        self.assertEqual(res, 10)

    def test_perimeter_zero_b(self):
        res = perimeter(10, 0, 10)
        self.assertEqual(res, 10)

    def test_perimeter_zero_c(self):
        res = perimeter(10, 10, 0)
        self.assertEqual(res, 10)

    def test_perimeter_square(self):
        res = perimeter(10, 10, 10)
        self.assertEqual(res, 30)

    def test_perimeter_str_arg_a(self):
        self.assertRaises(perimeter("10", 10, 10), Exception)

    def test_perimeter_str_arg_b(self):
        self.assertRaises(perimeter(10, "10", 10), Exception)

    def test_perimeter_str_arg_c(self):
        self.assertRaises(perimeter(10, 10, "10"), Exception)

    def test_perimeter_str_arg(self):
        rself.assertRaises(perimeter("10", "10", "10"), Exception)

    def test_perimeter_arr_arg_a(self):
        self.assertRaises(perimeter([10], 10, 10), Exception)

    def test_perimeter_arr_arg_b(self):
        self.assertRaises(perimeter(10, [10], 10), Exception)

    def test_perimeter_arr_arg_c(self):
        self.assertRaises(perimeter(10, 10, [10]), Exception)

    def test_perimeter_arr_arg(self):
        self.assertRaises(perimeter([10], [10], [10]), Exception)

    def test_perimeter_neg_arg_a(self):
        self.assertRaises(perimeter(-10, 10, 10), Exception)

    def test_perimeter_neg_arg_b(self):
        self.assertRaises(perimeter(10, -10, 10), Exception)

    def test_perimeter_neg_arg_c(self):
        self.assertRaises(perimeter(10, 10, -10), Exception)

    def test_perimeter_neg_arg(self):
        self.assertRaises(perimeter(-10, -10, -10), Exception)

    def test_perimeter_big_num(self):
        res = perimeter(2147483647, 2147483647, 2147483647)
        self.assertEqual(res, 6442450941)

    def test_perimeter_float_num(self):
        res = perimeter(10.0, 12.0, 10)
        self.assertEqual(res, 22.0)

    def test_perimeter_big_float_num(self):
        res = perimeter(0.00000000000000000001, 0.00000000000000000001, 0.00000000000000000001)
        self.assertEqual(res, 0.00000000000000000003)

    def test_perimeter_float_num_a(self):
        res = perimeter(0.000000001, 0.000000001, 0.000000001)
        self.assertEqual(res, 0.000000003)

    def test_perimeter_float_num_b(self):
        res = perimeter(10, 0.000000001, 10)
        self.assertEqual(res, 20.000000001)
