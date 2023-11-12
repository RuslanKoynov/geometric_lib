import random, unittest
def area(a, b): 
    '''
    Вычисление площади прямоугольника
    Параметры:
        a, b(int/float) - длина и ширина прямоугольника
    Возвращаемое значение:
        a * b(int/float) - площадь прямоугольника
    Пример вызова:
        area(2, 3) = 6
    '''
    return a * b 

def perimeter(a, b): 
    '''
    Вычисление периметра прямоугольника
    Параметры:
        a, b(int/float) - длина и ширина прямоугольника
    Возвращаемое значение:
        2 * (a + b) (int/float) - периметр прямоугольника
    Пример вызова:
        perimeter(2, 3) = 10
    '''
    return 2*(a + b) 

class RectangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(10, 0)
        self.assertEqual(res, 0)   
    def test_square_area(self):
        res = area(10, 10)
        self.assertEqual(res, 100)
    def test_small_numbers_area(self):
        res = area(1, 15)
        self.assertEqual(res, 15)