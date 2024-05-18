import unittest
class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
       res = area(0)
       self.assertEqual(res, 0)
       
    def test_area(self):
       res = area(6)
       self.assertEqual(res, 36)

    def test_area_large_number(self):
       res = area(13482830)
       self.assertEqual(res, 181786704808900)
    
    def test_perimeter_zero(self):
       res = perimeter(0)
       self.assertEqual(res, 0)

    def test_perimeter_equal(self):
       res = perimeter(10)
       self.assertEqual(res, 40)

    def test_perimeter_large_numbers(self):
       res = perimeter(13482830)
       self.assertEqual(res, 53931320)



def area(a):
    '''Принимает число a (сторона квадрата) и возвращает площадь квадрата по формуле S = a^2
    
    Параметры:
            a (int): десятичное целое число

        Возвращаемое значение:
            area_result (int) : целое число a во второй степени
            
        Пример вызова:
            print(area(6))
            > 36
    '''
    area_result = a * a
    return area_result


def perimeter(a):
    '''Принимает число a (сторона квадрата) и возвращает периметр квадрата по формуле P = 4a
    
    Параметры:
            a (int): десятичное целое число

        Возвращаемое значение:
            perimeter_result (int) : целое число a, умноженное на 4
            
        Пример вызова:
            print(perimeter(5))
            > 20
    '''
    perimeter_result = 4 * a
    return perimeter_result
