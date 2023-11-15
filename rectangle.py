import unittest


def area(a, b):
     '''
    Возвращает площадь прямоугольника

        Параметры:
            a (int): сторона прямоугольика
            b (int): сторона прямоугольника
        Возвращаемое значение:
            a*b (площадь прямоугольника)
    
    '''
     return a * b 

def perimeter(a, b):
    '''
    Возвращает периметр прямоугольника

        Параметры:
            a (int): сторона прямоугольника
            b (int): сторона прямоугольника
        Возвращаемое значение:
            удвоенная сумма a и b (периметр прямоугольника)
    
    '''
    return (a + b) * 2


class RectangleTestCase(unittest.TestCase):
     
     def test_area_positive_values(self):
          res = area(5,10)
          self.assertEqual(res,50)
          
     def test_area_negative_values(self):
        res = area(-5, 10)
        self.assertEqual(res, 0)

     def test_perimeter_zero_values(self):
        res = perimeter(0, 0)

        self.assertEqual(res, 0)
        
     def test_perimeter_mixed_values(self):
        res = perimeter(3, 7)
        self.assertEqual(res, 20)

     def test_area_float_values(self):
        res = area(2.5, 4)
        self.assertEqual(res, 10)

     def test_perimeter_float_values(self):
        res = perimeter(3, 4.5)
        self.assertEqual(res, 15)


if __name__ == '__main__':
    unittest.main()





        
