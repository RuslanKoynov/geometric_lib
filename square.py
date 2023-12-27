
def area(a):
    '''
    Вычисляет площадь квадрата.

    Параметры:
        a (float) - сторона квадрата
    Возвращаемое значение:
        float - площадь квадрата
    '''
    if isinstance(a, bool) or (not isinstance(a, float) and not isinstance(a, int)) or a <= 0:
        raise Exception
    
    return a * a


def perimeter(a):
    '''
    Вычисляет периметр квадрата.

    Параметры:
        a (float) - сторона квадрата
    Возвращаемое значение:
        float - периметр квадрата
    '''
    if isinstance(a, bool) or (not isinstance(a, float) and not isinstance(a, int)) or a <= 0:
        raise Exception
    
    return 4 * a
