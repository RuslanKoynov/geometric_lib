import math
import unittest

def area(r):
    '''
    Функция, для вычисления площади круга радиуса r.
    
        Параметры:
            r(int, float) - число (радиус круга)
        Возвращаемое значение:
            area(float) - площадь круга радиусом r
            
    Пример вызова функции:
        area(3) ==> 28.274333882308138
        area(1.4) ==> 6.157521601035994
    '''
    return math.pi * r * r
    
def perimeter(r):
    '''
    Функция, для вычисления длины окружности радиуса r.

        Параметры:
            r(int, float) - число (радиус круга)
        Возвращаемое значение:
            perimiter(float) - длина окружности с радиусом r

    Пример вызова функции:
        perimiter(5) ==> 31.41592653589793
        perimiter(2.5) ==> 15.707963267948966
    '''
    return 2 * math.pi * r

class TestStringMethods(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(3), 28.274333882308138)
        self.assertEqual(area(1.4), 6.157521601035994)
        self.assertNotEqual(area(8.65), 16)

    def test_perimeter(self):
        self.assertEqual(perimeter(5), 31.41592653589793)
        self.assertEqual(perimeter(2.5), 15.707963267948966)
        self.assertNotEqual(perimeter(6.31), 10.2)

if __name__ == '__main__':
    unittest.main()
