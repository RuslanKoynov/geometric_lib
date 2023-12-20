import unittest
import circle

class TestCircle(unittest.TestCase):

    # Проверка на площадь круга

    def test_area_negative_three(self):
        '''
        Тест для проверки вычисления площади круга с отрицательным радиусом.
        '''
        res = circle.area(-3)
        self.assertEqual(res, 28.274333882308138)

    def test_area_zero(self):
        '''
        Тест для проверки вычисления площади круга с нулевым радиусом.
        '''        
        res = circle.area(0)
        self.assertEqual(res, 0)

    def test_area_one(self):
        '''
        Тест для проверки вычисления площади круга с положительным радиусом.
        '''
        res = circle.area(1)
        self.assertEqual(res, 3.141592653589793)

    def test_area_five(self):
        '''
        Тест для проверки вычисления площади круга с положительным радиусом.
        '''
        res = circle.area(5)
        self.assertEqual(res, 78.53981633974483)

    # Проверка на периметр круга

    def test_perimeter_negative_three(self):
        '''
        Тест для проверки вычисления периметра круга с отрицательным радиусом.
        '''
        res = circle.perimeter(-3)
        self.assertEqual(res, -18.84955592153876)

    def test_perimeter_zero(self):
        '''
        Тест для проверки вычисления периметра круга с нулевым радиусом.
        '''
        res = circle.perimeter(0)
        self.assertEqual(res, 0.0)

    def test_perimeter_one(self):
        '''
        Тест для проверки вычисления периметра круга с положительным радиусом.
        '''
        res = circle.perimeter(1)
        self.assertEqual(res, 6.283185307179586)

    def test_perimeter_five(self):
        '''
        Тест для проверки вычисления периметра круга с положительным радиусом.
        '''
        res = circle.perimeter(5)
        self.assertEqual(res, 31.41592653589793)