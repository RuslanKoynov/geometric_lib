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
    return a + b + c

def median(a, b, c):
    '''
    Вычисляет длину медианы треугольника по трём сторонам.

    Параметры:
        a (float) - сторона, к которой проведена медиана
        b (float) - вторая сторона треугольника
        c (float) - третья сторона треугольника
    Возвращаемое значение:
        float - длину медианы треугольника

    Для вычисления длины медианы используется следующая формула:
    m = sqrt(2b^2 + 2c^2 - a^2) / 2
    '''
    return math.sqrt(2*b*b + 2*c*c - a*a) / 2