def area(a, b):
    '''
    Вычисляет площадь прямоугольника.

    Параметры:
        a (float) - первая сторона прямоугольника
        b (float) - вторая сторона прямоугольника
    Возвращаемое значение:
        float - площадь прямоугольника
    '''
    if isinstance(a, bool) or isinstance(b, bool) or (not isinstance(a, float) and not isinstance(a, int)) or (not isinstance(b, int) and not isinstance(b, float)) or a <= 0 or b <= 0:
        raise Exception
    
    return a * b 

def perimeter(a, b):
    '''
    Вычисляет периметр прямоугольника.

    Параметры:
        a (float) - первая сторона прямоугольника
        b (float) - вторая сторона прямоугольника
    Возвращаемое значение:
        float - периметр прямоугольника
    '''
    if isinstance(a, bool) or isinstance(b, bool) or (not isinstance(a, float) and not isinstance(a, int)) or (not isinstance(b, int) and not isinstance(b, float)) or a <= 0 or b <= 0:
        raise Exception
    
    return (a + b) * 2