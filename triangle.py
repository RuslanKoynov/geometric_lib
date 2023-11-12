import unittest, random
def area(a, h):
    '''
    Вычисление площади треугольника
    Параметры:
        h, a(int/float) - высота и сторона(основание)
    Возвращаемое значение:
        a * h / 2(int/float) - площадь треугольника
    Пример вызова:
        area(2, 4) = 4
    '''
    return a * h / 2 

def perimeter(a, b, c):
    '''
    Вычисление периметра треугольника
    Параметры:
        a, b, c(int/float) - 3 стороны треугольника
    Возвращаемое значение:
        a + b + c(int/float) - площадь треугольника
    Пример вызова:
        perimeter(3, 4, 5) = 12
    ''' 
    return a + b + c 

class TriangleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0, 0)
        self.assertEqual(res, 0)
    def test_small_numbers_area(self):
        res = area(15, 2)
        self.assertEqual(res, 15*2/2)
    def test_big_numbers_area(self):
        res = area(6173391, 126381732)
        self.assertEqual(res, 6173391*126381732/2)
    def test_small_random_number_area(self):
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        res = area(a, b)
        self.assertEqual(res, a*b/2)
    def test_big_random_number_area(self):
        a = random.randint(1000, 10000000)
        b = random.randint(1000, 10000000)
        res = area(a, b)
        self.assertEqual(res, a*b/2)   
    def test_zero_perim(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)
    def test_small_numbers_perim(self):
        res = perimeter(15, 10, 5)
        self.assertEqual(res, 15+10+5)
    def test_big_numbers_perim(self):
        res = perimeter(6173391, 126371832, 981331)
        self.assertEqual(res, 6173391+126371832+981331)
    def test_small_random_number_perim(self):
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        c = random.randint(1, 20)
        res = perimeter(a, b, c)
        self.assertEqual(res, a+b+c)
    def test_big_random_number_perim(self):
        a = random.randint(1000, 10000000)
        b = random.randint(1000, 10000000)
        c = random.randint(1000, 10000000)
        res = perimeter(a, b, c)
        self.assertEqual(res, a+b+c)