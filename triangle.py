def area(a, h):
    '''
          Принимает два числа:
           a - длина стороны треугольника
           h - длина высоты треугольника, опущенной к стороне a
          Возвращает значение площади треугольника по формуле: площадь треугольника равна половине произведения его основания на
          высоту
          Примеры вызова:
          Входные данные:    Выходные данные:
          area(5, 2)         = 5
          area(6, 4)         = 12
          area(8, 5)         = 20
    '''
    return a * h / 2

def perimeter(a, b, c):
    '''
           Принимает три числа a, b и c - длины трех сторон треугольника
           Возвращает значение периметра треугольника - сумму его трёх сторон
           Примеры вызова:
           Входные данные:       Выходные данные:
           perimeter(3, 4, 5)    = 12
           perimeter(12, 13, 5)  = 30
           perimeter(4, 4, 5)    = 13
    '''
    return a + b + c