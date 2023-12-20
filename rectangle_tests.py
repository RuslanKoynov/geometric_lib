import unittest
import rectangle

class TestRectangle(unittest.TestCase):

    # Проверка на площадь треугольника

    def test_area_negative_three(self):
        '''
        Тест для проверки вычисления площади треугольника с отрицательными сторонами треугольника.
        '''
        res = rectangle.area(-3, -3)
        self.assertAlmostEqual(res, 9)

    def test_area_zero(self):
        '''
        Тест для проверки вычисления площади треугольника с нулевыми сторонами треугольника.
        '''        
        res = rectangle.area(0, 0)
        self.assertAlmostEqual(res, 0)

    def test_area_one(self):
        '''
        Тест для проверки вычисления площади треугольника с положительными сторонами треугольника.
        '''
        res = rectangle.area(1, 1)
        self.assertAlmostEqual(res, 1)

    def test_area_five(self):
        '''
        Тест для проверки вычисления площади треугольника с положительными сторонами треугольника.
        '''
        res = rectangle.area(5, 5)
        self.assertAlmostEqual(res, 24)

    # Проверка на периметр треугольника

    def test_perimeter_negative_three(self):
        '''
        Тест для проверки вычисления периметра треугольника с отрицательными сторонами треугольника.
        '''
        res = rectangle.perimeter(-3, -3)
        self.assertAlmostEqual(res, -11)

    def test_perimeter_zero(self):
        '''
        Тест для проверки вычисления периметра треугольника с нулевыми сторонами треугольника.
        '''
        res = rectangle.perimeter(0, 0)
        self.assertAlmostEqual(res, 0.0)

    def test_perimeter_one(self):
        '''
        Тест для проверки вычисления периметра треугольника с положительными сторонами треугольника.
        '''
        res = rectangle.perimeter(1, 1)
        self.assertAlmostEqual(res, 4)

    def test_perimeter_five(self):
        '''
        Тест для проверки вычисления периметра треугольника с положительными сторонами треугольника.
        '''
        res = rectangle.perimeter(5, 5)
        self.assertAlmostEqual(res, 20)