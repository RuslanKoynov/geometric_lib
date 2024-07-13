import unittest
import circle

class TestCircle(unittest.TestCase):

    # Проверка на площадь круга

    def test_area_negative_three(self):
        '''
        Тест для проверки вычисления площади круга с отрицательным радиусом.
        '''
        with self.assertRaises(TypeError):
            circle.area(-3)

    def test_area_zero(self):
        '''
        Тест для проверки вычисления площади круга с нулевым радиусом.
        '''        
        res = circle.area(0)
        self.assertAlmostEqual(res, 0.0)

    def test_area_one(self):
        '''
        Тест для проверки вычисления площади круга с положительным радиусом.
        '''
        res = circle.area(1)
        self.assertAlmostEqual(res, 3.14, places=2)

    def test_area_five(self):
        '''
        Тест для проверки вычисления площади круга с положительным радиусом.
        '''
        res = circle.area(5)
        self.assertAlmostEqual(res, 78.53, places=1)

    # Проверка на периметр круга

    def test_perimeter_negative_three(self):
        '''
        Тест для проверки вычисления периметра круга с отрицательным радиусом.
        '''
        with self.assertRaises(TypeError):
            circle.perimeter(-3)

    def test_perimeter_zero(self):
        '''
        Тест для проверки вычисления периметра круга с нулевым радиусом.
        '''
        res = circle.perimeter(0)
        self.assertAlmostEqual(res, 0)

    def test_perimeter_one(self):
        '''
        Тест для проверки вычисления периметра круга с положительным радиусом.
        '''
        res = circle.perimeter(1)
        self.assertAlmostEqual(res, 6.28, places=2)

    def test_perimeter_five(self):
        '''
        Тест для проверки вычисления периметра круга с положительным радиусом.
        '''
        res = circle.perimeter(5)
        self.assertAlmostEqual(res, 31.41, places=1)