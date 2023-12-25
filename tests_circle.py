import unittest
import circle

class TestCircle(unittest.TestCase):


    # Проверка на площадь круга

    def test_area_zero(self):
        '''
        Тест для проверки вычисления площади круга с нулевым радиусом.
        '''
        r = circle.area(0)
        self.assertAlmostEqual(r, 0)

    def test_area_negative_five(self):
        '''
        Тест для проверки вычисления площади круга с отрицательным радиусом.
        '''
        r = circle.area(-5)
        self.assertAlmostEqual(r, 78.53981633974483)

    def test_area_five(self):
        '''
        Тест для проверки вычисления площади круга с положительным радиусом.
        '''
        r = circle.area(5)
        self.assertAlmostEqual(r, 78.53981633974483)

    # Проверка на периметр круга

    def test_perimeter_zero(self):
        '''
        Тест для проверки вычисления периметра круга с нулевым радиусом.
        '''
        r = circle.perimeter(0)
        self.assertAlmostEqual(r, 0.0)

    def test_perimeter_negative_five(self):
        '''
        Тест для проверки вычисления периметра круга с отрицательным радиусом.
        '''
        r = circle.perimeter(-5)
        self.assertAlmostEqual(r, -31.41592653589793)

    def test_perimeter_five(self):
        '''
        Тест для проверки вычисления периметра круга с положительным радиусом.
        '''
        r = circle.perimeter(5)
        self.assertAlmostEqual(r, 31.41592653589793)

