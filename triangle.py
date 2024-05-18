import unittest
class TriangleTestCase(unittest.TestCase):
    def test_area_zero(self):
       res = area(10, 0)
       self.assertEqual(res, 0)
       
    def test_area_equal(self):
       res = area(6, 6)
       self.assertEqual(res, 18)

    def test_area_large_numbers(self):
       res = area(13482830, 49234924)
       self.assertEqual(res, 331913055177460)
    
    def test_perimeter_zero(self):
       res = perimeter(10, 0, 10)
       self.assertEqual(res, 20)

    def test_perimeter_equal(self):
       res = perimeter(10, 10, 10)
       self.assertEqual(res, 30)

    def test_perimeter_large_numbers(self):
       res = perimeter(13482830, 49234924, 39392839)
       self.assertEqual(res, 102110593)



def area(a, h):
    '''Принимает числа a, h (a - катет, h - высота) и возвращает площадь треугольника по формуле S = (1/2)ah
    
    Параметры:
            a (int): первое десятичное целое число
            h (int): второе десятичное целое число

        Возвращаемое значение:
            area_result (float) : половина от произведения целых чисел a и h

        Пример вызова:
            print(area(10, 4))
            > 20
    '''
    area_result = a * h / 2
    return area_result

def perimeter(a, b, c):
    '''Принимает числа a, b, c (стороны треугольника) и возвращает периметр треугольника по формуле P = a + b + c
    
    Параметры:
            a (int): первое десятичное целое число
            b (int): второе десятичное целое число
            c (int): третье десятичное целое число

        Возвращаемое значение:
            perimeter_result (int) : сумма трёх целых чисел a, b, c

        Пример вызова:
            print(perimeter(3, 4, 5))
            > 12
    '''
    perimeter_result = a + b + c
    return perimeter_result
