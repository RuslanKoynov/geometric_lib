import math
import unittest
class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
       res = area(0)
       self.assertEqual(res, 0)
       
    def test_area(self):
       res = area(10)
       self.assertEqual(res, 314.1592653589793)

    def test_area_large_numbers(self):
       res = area(13482830)
       self.assertEqual(res, 571099776347936.5783503937)
    
    def test_circumference_zero(self):
       res = circumference(0)
       self.assertEqual(res, 0)
       
    def test_circumference(self):
       res = circumference(10)
       self.assertEqual(res, 62.83185307179586)

    def test_circumference_large_numbers(self):
       res = circumference(13482830)
       self.assertEqual(res, 84715119.3552001439)



def area(r):
    '''Принимает число r (радиус) и возвращает площадь круга по формуле S = πr^2
    
        Параметры:
            r (int): десятичное целое число

        Возвращаемое значение:
            area_result (int) : целое число r во второй степени, умноженное на число π

        Пример вызова:
            print(area(2))
            > 12.566370614359172
    '''
    area_result = math.pi * r * r
    return area_result


def circumference(r):
    '''Принимает число r (радиус) и возвращает периметр круга по формуле C = 2πr
    
        Параметры:
            r (int): десятичное целое число

        Возвращаемое значение:
            circumference_result (int) : удвоенное произведение целого числа r, умноженного на число π

        Пример вызова:
            print(circumference(3))
            > 18.84955592153876
    '''
    circumference_result = 2 * math.pi * r
    return circumference_result

