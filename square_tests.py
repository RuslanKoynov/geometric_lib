import unittest
import square

class TestSquare(unittest.TestCase):

    # Проверка на площадь квадрата

    def test_area_negative_three(self):
        '''
        Тест для проверки вычисления площади квадрата с отрицательными стороной.
        '''
        res = square.area(-3)
        self.assertAlmostEqual(res, 9)

    def test_area_zero(self):
        '''
        Тест для проверки вычисления площади квадрата с нулевой стороной.
        '''        
        res = square.area(0)
        self.assertAlmostEqual(res, 0)

    def test_area_one(self):
        '''
        Тест для проверки вычисления площади квадрата с положительной стороной.
        '''
        res = square.area(1)
        self.assertAlmostEqual(res, 1)

    def test_area_five(self):
        '''
        Тест для проверки вычисления площади квадрата с положительной стороной.
        '''
        res = square.area(5)
        self.assertAlmostEqual(res, 25)

    # Проверка на периметр квадрата

    def test_perimeter_negative_three(self):
        '''
        Тест для проверки вычисления периметра квадрата с отрицательными стороной.
        '''
        res = square.perimeter(-3)
        self.assertAlmostEqual(res, -12)

    def test_perimeter_zero(self):
        '''
        Тест для проверки вычисления периметра квадрата с нулевой стороной.
        '''  
        res = square.perimeter(0)
        self.assertAlmostEqual(res, 0)

    def test_perimeter_one(self):
        '''
        Тест для проверки вычисления периметра квадрата с положительной стороной.
        '''
        res = square.perimeter(1)
        self.assertAlmostEqual(res, 4)

    def test_perimeter_five(self):
        '''
        Тест для проверки вычисления периметра квадрата с положительной стороной.
        '''
        res = square.perimeter(5)
        self.assertAlmostEqual(res, 20)
