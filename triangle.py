import unittest

def area(a, h): 
    return a * h / 2 

def perimeter(a, b, c): 
    return a + b + c 


class TriangleTest(unittest.TestCase):
    def test_area_zero(self):
        '''
        Тестирование функции площади при вводе 0
        '''
        self.assertEqual(area(0, 10), 0)
    def test_area_float(self):
        '''
        Тестирование функции площади при вводе числа с плавающей точкой
        '''
        self.assertAlmostEqual(area(3.5, 6), 10.5, places=2)
    def test_area_negativenum(self):
        '''
        Тестирование функции площади при вводе отрицательных чисел
        '''
        with self.assertRaises(Exception):
            area(-5, 7)
    def test_area_positivenum(self):
        '''
        Тестирование функции площади при вводе положительных чисел
        '''
        self.assertEqual(area(4, 8), 16)


    def test_perimeter_zero(self):
        '''
        Тестирование функции периметра при вводе 0
        '''
        self.assertEqual(perimeter(0, 0, 0), 0)
    def test_perimeter_float(self):
        '''
        Тестирование функции периметра при вводе числа с плавающей точкой
        '''
        self.assertAlmostEqual(perimeter(2.5, 3, 4.5), 10, places=2)
    def test_perimeter_negativenum(self):
        '''
        Тестирование функции периметра при вводе отрицательных чисел
        '''
        with self.assertRaises(Exception):
            perimeter(-2, -3, -4)
    def test_perimeter_positivenum(self):
        '''
        Тестирование функции периметра при вводе положительных чисел
        '''
        self.assertEqual(perimeter(3, 4, 5), 12)

if __name__ == '__main__':
    unittest.main()
    
