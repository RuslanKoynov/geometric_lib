import math
import unittest

def area(r):
    return math.pi * r * r


def perimeter(r):
    return 2 * math.pi * r


class CircleTest(unittest.TestCase):
    def test_area_zero(self):
        '''
        Тестирование функции площади при вводе 0
        '''
        self.assertEqual(area(0), 0)
    def test_area_float(self):
        '''
        Тестирование функции площади при вводе числа с плавающей точкой
        '''
        self.assertEqual(area(3.5), math.pi * 3.5 * 3.5)
    def test_area_negativenum(self):
        '''
        Тестирование функции площади при вводе отрицательных чисел
        '''
        with self.assertRaises(Exception):
            area(-7)
    def test_area_positivenum(self):
        '''
        Тестирование функции площади при вводе положительных чисел
        '''
        self.assertEqual(area(7), math.pi * 7 * 7)
        

    def test_perimeter_zero(self):
        '''
        Тестирование функции периметра при вводе 0
        '''
        self.assertEqual(perimeter(0), 0)
    def test_perimeter_float(self):
        '''
        Тестирование функции периметра при вводе числа с плавающей точкой
        '''
        self.assertEqual(perimeter(3.5), 2 * math.pi * 3.5)
    def test_perimeter_negativenum(self):
        '''
        Тестирование функции периметра при вводе отрицательных чисел
        '''
        with self.assertRaises(Exception):
            perimeter(-7)
    def test_perimeter_positivenum(self):
        '''
        Тестирование функции периметра при вводе положительных чисел
        '''
        self.assertEqual(perimeter(7), 2 * math.pi * 7)

if __name__ == '__main__':
    unittest.main()
    
