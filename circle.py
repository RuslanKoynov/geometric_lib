import math, unittest, random

def area(r):
    '''
    Вычисление площади круга
    Параметр:
        r(int/float) - радиус круга
        math.pi(float) - число пи
    Возвращаемое значение:
        math.pi * r * r(float) - Площадь круга
    Пример вызова:
        area(10) = 314.1592653589793
    '''
    return math.pi * r * r

def perimeter(r):
    '''
    Вычисление периметра
    Параметр:
        r(int/float) - радиус круга
        math.pi(float) - число пи
    Вовзращаемое значение:
        2 * math.pi * r(float) - Периметр круга
    Пример вызова:
        perimeter(10) = 62.83185307179586
    '''
    return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):
    def test_zero_area(self):
        res = area(0)
        self.assertEqual(res, 0)
    def test_small_numbers_area(self):
        res = area(15)
        self.assertEqual(res, math.pi * 15**2)
    def test_small_numbers_area(self):
        res = area(6173391)
        self.assertEqual(res, math.pi*6173391**2)
    def test_small_random_number_area(self):
        a = random.randint(1, 20)
        res = area(a)
        self.assertEqual(res, math.pi*a**2)
    def test_big_random_number_area(self):
        a = random.randint(1000, 10000000)
        res = area(a)
        self.assertEqual(res, math.pi*a**2)
    def test_zero_perim(self):
        res = perimeter(0)
        self.assertEqual(res, 0)
    def test_small_numbers_perim(self):
        res = perimeter(15)
        self.assertEqual(res, 2*math.pi*15)
    def test_small_numbers_perim(self):
        res = perimeter(6173391)
        self.assertEqual(res, 2*math.pi*6173391)
    def test_small_random_number_perim(self):
        a = random.randint(1, 20)
        res = perimeter(a)
        self.assertEqual(res, 2*math.pi*a)