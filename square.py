import unittest

def area(a):
    return a * a

def perimeter(a):
    return 4 * a

class SquareTest(unittest.TestCase):
    def test_area_positivenum(self):
        '''
        Тестирование функции площади при вводе положительных чисел
        '''
        self.assertEqual(area(6), 36)
    def test_area_float(self):
        '''
        Тестирование функции площади при вводе числа с плавающей точкой
        '''
        self.assertAlmostEqual(area(6.9), 47.61, places=2)
    def test_area_zero(self):
        '''
        Тестирование функции площади при вводе 0
        '''
        self.assertEqual(area(0), 0)
    def test_area_negativenum(self):
        '''
        Тестирование функции площади при вводе отрицательных чисел
        '''
        with self.assertRaises(Exception):
            area(-7)

    def test_perimeter_positivenum(self):
        '''
        Тестирование функции периметра при вводе положительных чисел
        '''
        self.assertEqual(perimeter(4), 16)
    def test_perimeter_float(self):
        '''
        Тестирование функции периметра при вводе числа с плавающей точкой
        '''
        self.assertEqual(perimeter(2.3), 9.2)
    def test_perimeter_zero(self):
        '''
        Тестирование функции периметра при вводе 0
        '''
        self.assertEqual(perimeter(0), 0)
    def test_perimeter_negativenum(self):
        '''
        Тестирование функции периметра при вводе отрицательных чисел
        '''
        with self.assertRaises(Exception):
            perimeter(-5)


if __name__ == '__main__':
    unittest.main()
