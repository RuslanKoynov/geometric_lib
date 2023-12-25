import unittest
import square

class TestSquare(unittest.TestCase):

    # Проверка на площадь квадрата

    def test_area_negative_four(self):
        '''
        Тест для проверки вычисления площади квадрата с отрицательными стороной.
        '''
        res = square.area(-4)
        self.assertAlmostEqual(res, 16)

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

    def test_area_six(self):
        '''
        Тест для проверки вычисления площади квадрата с положительной стороной.
        '''
        res = square.area(6)
        self.assertAlmostEqual(res, 36)

    # Проверка на периметр квадрата

    def test_perimeter_negative_four(self):
        '''
        Тест для проверки вычисления периметра квадрата с отрицательными стороной.
        '''
        res = square.perimeter(-4)
        self.assertAlmostEqual(res, -16)

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

    def test_perimeter_six(self):
        '''
        Тест для проверки вычисления периметра квадрата с положительной стороной.
        '''
        res = square.perimeter(6)
        self.assertAlmostEqual(res, 24)