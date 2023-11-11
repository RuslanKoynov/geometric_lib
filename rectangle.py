def area(a, b): 
    '''
    Возвращает площадь прямоугольника длины a и ширины b

        Параметры:
            a (int/float): длина прямоугольника
            b (int/float): ширина прямоугольника

        Возвращаемое значение (int/float):
            Площадь прямоугольника по математической формуле            
    '''

    if all(isinstance(x, int | float) and x >= 0 for x in [a, b]):
        return a * b 
    
    return ValueError

def perimeter(a, b): 
    '''
    Возвращает периметр прямоугольника длина a и ширины b

        Параметры:
            a (int/float): длина прямоугольника
            b (int/float): ширина прямоугольника

        Возвращаемое значение (int/float):
            периметр прямоугольника по математической формуле
    '''

    if all(isinstance(x, int | float) and x > 0 for x in [a, b]):
        return 2 * (a + b)
    
    return ValueError

