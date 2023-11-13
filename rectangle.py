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

    def test_big_numbers_area(self):
        res = area(6173391, 1572631732)
        self.assertEqual(res, 9708470580643212)

    def test_small_random_number_area(self):
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        res = area(a, b)
        self.assertEqual(res, a * b)

    def test_big_random_number_area(self):
        a = random.randint(1000, 10000000)
        b = random.randint(1000, 10000000)
        res = area(a, b)
        self.assertEqual(res, a * b)

    def test_zero_perim(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_same_numbers_perim(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)

    def test_small_numbers_perim(self):
        res = perimeter(1, 15)
        self.assertEqual(res, 32)

    def test_big_numbers_perim(self):
        res = perimeter(6173391, 1572631732)
        self.assertEqual(res, 3157610246)

    def test_small_random_number_perim(self):
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        res = perimeter(a, b)
        self.assertEqual(res, 2 * (a + b))

    def test_big_random_number_perim(self):
        a = random.randint(1000, 10000000)
        b = random.randint(1000, 10000000)
        res = perimeter(a, b)
        self.assertEqual(res, 2 * (a + b))