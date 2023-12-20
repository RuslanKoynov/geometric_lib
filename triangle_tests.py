import unittest
import triangle

class TestTriangle(unittest.TestCase):

    # Проверка на площадь треугольника

    def test_area_negative_three(self):
        '''
        Тест для проверки вычисления площади треугольника с отрицательными числами.
        '''
        res = triangle.area(-3, -3)
        self.assertEqual(res, 4.5)

    def test_area_zero(self):
        '''
        Тест для проверки вычисления площади треугольника с нулевыми числами.
        '''        
        res = triangle.area(0, 0)
        self.assertEqual(res, 0.0)

    def test_area_one(self):
        '''
        Тест для проверки вычисления площади треугольника с положительными числами.
        '''
        res = triangle.area(1, 1)
        self.assertEqual(res, 0.5)

    def test_area_five(self):
        '''
        Тест для проверки вычисления площади треугольника с положительными числами.
        '''
        res = triangle.area(5, 5)
        self.assertEqual(res, 12.5)

    # Проверка на периметр треугольника

    def test_perimeter_negative_three(self):
        '''
        Тест для проверки вычисления периметра треугольника с отрицательными числами.
        '''
        res = triangle.perimeter(-3, -3, -3)
        self.assertEqual(res, -9)

    def test_perimeter_zero(self):
        '''
        Тест для проверки вычисления периметра треугольника с нулевыми числами.
        '''
        res = triangle.perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_one(self):
        '''
        Тест для проверки вычисления периметра треугольника с положительными числами.
        '''
        res = triangle.perimeter(1, 1, 1)
        self.assertEqual(res, 3)

    def test_perimeter_five(self):
        '''
        Тест для проверки вычисления периметра треугольника с положительными числами.
        '''
        res = triangle.perimeter(5, 5, 5)
        self.assertEqual(res, 15)
