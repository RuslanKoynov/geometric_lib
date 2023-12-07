import unittest

def area(a, b): 
    return a * b 

def perimeter(a, b): 
    return (a + b) * 2

class RectangleTests(unittest.TestCase):
    def test_area_positivenum(self):
        '''
        Тестирование функции площади при вводе положительных чисел
        '''
        self.assertEqual(area(5, 4), 20)
    def test_area_float(self):
        '''
        Тестирование функции площади при вводе числа с плавающей точкой
        '''
        self.assertEqual(area(5.3, 2), 10.6)
    def test_area_zero(self):
        '''
        Тестирование функции площади при вводе 0
        '''
        self.assertEqual(area(0, 5), 0)
    def test_area_negativenum(self):
        '''
        Тестирование функции площади при вводе отрицательных чисел
        '''
        with self.assertRaises(Exception):
            area(-6, -6)

    def test_perimeter_positivenum(self):
        '''
        Тестирование функции периметра при вводе положительных чисел
        '''
        self.assertEqual(perimeter(3, 4), 14)
    def test_perimeter_float(self):
        '''
        Тестирование функции периметра при вводе числа с плавающей точкой
        '''
        self.assertEqual(perimeter(5.3, 2), 14.6)
    def test_perimeter_zero(self):
        '''
        Тестирование функции периметра при вводе 0
        '''
        self.assertEqual(perimeter(0, 8), 16)
    def test_perimeter_negativenum(self):
        '''
        Тестирование функции периметра при вводе отрицательных чисел
        '''
        with self.assertRaises(Exception):
            perimeter(-7, 9)


if __name__ == '__main__':
    unittest.main()
