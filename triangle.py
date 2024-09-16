def area(a, h):
    '''
    Возвращает площадь треугольника со стороной a и высотой h.

        Параметры:
            a (int): десятичное число - сторона треугольника
            h (int): десятичное число - высота треугольника, проведённая к стороне a

        Возвращаемое значение:
            a * h / 2 (float): число с плавающей точкой - площадь треуголника со стороной a и выостой h

    Пример вызова функции: area(10, 20) -> 100
    '''
    if isinstance(a, bool) or isinstance(h, bool):
        return 'Invalid input'
    if isinstance(a, str) or isinstance(h, str):
        return 'Invalid input'
    if a < 0 or h < 0:
        return 'Invalid input'
    if a == 0 or h == 0:
        return "The figure doesn't exist"
    return a * h / 2


def perimeter(a, b, c):
    '''
        Возвращает периметр треугольника со сторонами a, b, c.

            Параметры:
                a (int): десятичное число - первая сторона треугольника
                b (int): десятичное число - вторая сторона треугольника
                c (int): десятичное число - третье сторона треугольника

            Возвращаемое значение:
                a + b + c (int): целое число - периметр треуголника со сторонами a, b, c

        Пример вызова функции: perimeter(10, 20, 30) -> 60
        '''
    if isinstance(a, bool) or isinstance(b, bool) or isinstance(c, bool):
        return 'Invalid input'
    if isinstance(a, str) or isinstance(b, str) or isinstance(c, bool):
        return 'Invalid input'
    if a < 0 or b < 0:
        return 'Invalid input'
    if a == 0 or b == 0 or c == 0:
        return "The figure doesn't exist"
    elif (a + b) > c and (a + c) > b and (b + c) > a:
        return a + b + c
    else:
        return "The figure doesn't exist"
