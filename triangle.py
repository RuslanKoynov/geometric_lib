import math

def area(a, h):
    '''
    Вычисляет площадь треугольника.

    Параметры:
        a (float) - сторона треугольника
        h (float) - высота треугольника (проведённая к стороне a)
    Возвращаемое значение:
        float - площадь треугольника    
    '''
    if isinstance(a, bool) or isinstance(h, bool) or  not isinstance(a, int) or not isinstance(h, int) or a <= 0 or h <= 0:
        raise Exception
    
    return a * h / 2 

def perimeter(a, b, c): 
    '''
    Вычисляет периметр треугольника.

    Параметры:
        a (float) - первая сторона треугольника
        b (float) - вторая сторона треугольника
        c (float) - третья сторона треугольника
    Возвращаемое значение:
        float - периметр треугольника
    '''
    if isinstance(a, bool) or isinstance(b, bool) or isinstance(c, bool) or not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int) or a <= 0 or b <= 0 or c <= 0:
        raise Exception
    
    return a + b + c

def median(a, b, c):
    '''
    Вычисляет длину медианы треугольника по трём сторонам.

    Параметры:
        a (float) - сторона, к которой проведена медиана
        b (float) - вторая сторона треугольника
        c (float) - третья сторона треугольника
    Возвращаемое значение:
        float - длина медианы треугольника

    Для вычисления длины медианы используется следующая формула:
    m = sqrt(2b^2 + 2c^2 - a^2) / 2
    '''
    if isinstance(a, bool) or isinstance(b, bool) or isinstance(c, bool) or not isinstance(a, int) or not isinstance(b, int) or not isinstance(c, int) or a <= 0 or b <= 0 or c <= 0:
        raise Exception
    
    return math.sqrt(2*b*b + 2*c*c - a*a) / 2