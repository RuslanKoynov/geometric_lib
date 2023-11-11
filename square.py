
def area(a):
    '''
    Возвращает площадь квадрата с длиной стороны a

        Параметры:
            a (int/float): длина стороны квадрата

        Возвращаемое значение (int/float):
                площадь квадрата по математической формуле
    '''

    if isinstance(a, int | float) and a >= 0:
        return a * a
    
    return ValueError


def perimeter(a):
    '''
    Возвращает периметр квадрата с длиной стороны a

        Параметры:
             a (int/float): длина стороны квадрата

        Возвращаемое значение (int, float):
            периметр квадрата по математической формуле
    '''
    
    if isinstance(a, int | float) and a > 0:
        return 4 * a

    return ValueError
