import unittest
class RectangleTestCase(unittest.TestCase):
    def test_area_zero(self):
       res = area(10, 0)
       self.assertEqual(res, 0)
       
    def test_area_square(self):
       res = area(10, 10)
       self.assertEqual(res, 100)

    def test_area_large_numbers(self):
       res = area(13482830, 49234924)
       self.assertEqual(res, 663826110354920)
    
    def test_perimeter_zero(self):
       res = perimeter(10, 0)
       self.assertEqual(res, 20)
       
    def test_perimeter_square(self):
       res = perimeter(10, 10)
       self.assertEqual(res, 40)

    def test_perimeter_large_numbers(self):
       res = perimeter(13482830, 49234924)
       self.assertEqual(res, 125435508)



def area(a, b):
    '''Принимает числа a, b (стороны прямоугольника) и возвращает площадь прямоугольнкиа по формуле S = ab
    
        Параметры:
            a (int): первое десятичное целое число
            b (int): второе десятичное целое число

        Возвращаемое значение:
            area_result (int) : произведение целых чисел a и b

        Пример вызова:
            print(area(10, 5))
            > 50
    '''
    area_result = a * b
    return area_result

def perimeter(a, b):
    '''Принимает числа a, b (стороны прямоугольника) и возвращает периметр прямоугольнкиа по формуле P = 2(a+b)
    
        Параметры:
            a (int): первое десятичное целое число
            b (int): второе десятичное целое число

        Возвращаемое значение:
            perimeter_result (int) : удвоенная сумма целых чисел a и b

        Пример вызова:
            print(perimeter(10, 5))
            > 30
    '''
    perimeter_result = 2*(a+b)
    return perimeter_result
