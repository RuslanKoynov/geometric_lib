import unittest

def area(a):
    '''
    Функция, для вычисления площади квадрата со стороной a.

        Параметры:
            a(int, float) - число (сторона квадрата)
        Возвращаемое значение:
            area(int, float) - площадь квадрата со стороной a

    Пример вызова функции:
        area(10) ==> 100
        area(4.6) ==> 21.159999999999997
    '''
    return a * a

def perimeter(a):
    '''
    Функция, для вычисления периметра квадрата со стороной a.

        Параметры:
            a(int, float) - число (сторона квадрата)
        Возвращаемое значение:
            perimeter(int, float) - периметр квадрата со стороной a

    Пример вызова функции:
        perimeter(3) ==> 12
        perimeter(2.8) ==> 11.2
    '''
    return 4 * a

class TestStringMethods(unittest.TestCase):

    def test_area(self):
        self.assertEqual(area(12), 144)
        self.assertEqual(area(2.5), 6.25)
        self.assertNotEqual(area(9.0), 81.1)
        self.assertRaises(TypeError, area, 'ten', '9')

    def test_perimeter(self):
        self.assertEqual(perimeter(110), 440)
        self.assertEqual(perimeter(0), 0)
        self.assertNotEqual(perimeter(5.7), 21.1)
        self.assertRaises(TypeError, perimeter, 'nine', '10')

if __name__ == '__main__':
    unittest.main()
