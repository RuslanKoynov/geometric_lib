import unittest

def area(a, b):
    '''
    Функция, для вычисления площади прямоугольника со сторонами a и b

        Параметры:
            a,b(int, float) - числа (стороны прямоугольника)
        Возвращаемое значение:
            area(int, float) - площадь прямоугольника со сторонами a и b

    Пример вызова функции:
        area(7, 10) ==> 70
        area(2, 5.0) ==> 10.0
    '''
    return a * b

def perimeter(a, b):
    '''
    Функция, для вычисления периметра прямоугольники со сторонами a и b

        Параметры:
            a,b(int, float) - числа (стороны прямоугольника)
        Возвращаемое значение:
            perimeter(int, float) - периметр прямоугольника со сторонами a и b

    Пример вызова функции:
        perimeter(3, 6) ==> 18
        perimeter(2.8, 2.0) ==> 5.6
    '''
    return 2*(a + b)

class TestStringMethods(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(7, 7), 49)
        self.assertEqual(area(2.4, 3.65), 8.76)
        self.assertNotEqual(area(8.65, 4.183), 8)
        self.assertRaises(TypeError, area, 'nine', '7')

    def test_perimeter(self):
        self.assertEqual(perimeter(12, 3.5), 31)
        self.assertEqual(perimeter(2.25, 0), 4.5)
        self.assertNotEqual(perimeter(18, 3), 41)
        self.assertRaises(TypeError, perimeter, 'abc', 9)

if __name__ == '__main__':
    unittest.main()
