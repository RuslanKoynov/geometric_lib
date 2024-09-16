def area(a, b):
    '''
    Возваращает площадь прямоугольника со сторонами a и b.

        Параметры:
            a(int): десятичное число - большая сторона прямоугольника
            b(int): десятичное число - меньшая сторона прямоугольника

        Возвращаемое значение:
            a * b(int): целое число - площадь прямоугольника

    Пример вызова функции: area(10, 20) -> 200
    '''
    if isinstance(a, bool) or isinstance(b, bool):
        return 'Invalid input'
    if isinstance(a, str) or isinstance(b, str):
        return 'Invalid input'
    if a < 0 or b < 0:
        return 'Invalid input'
    if a == 0 or b == 0:
        return "The figure doesn't exist"
    return a * b


def perimeter(a, b):
    '''
    Возваращает периметр прямоугольника со сторонами a и b

        Параметры:
            a(int): десятичное число - большая сторона прямоугольника
            b(int): десятичное число - меньшая сторона прямоугольника

        Возвращаемое значение:
            2 * (a + b) (int): целое число - периметр прямоугольника

    Пример вызова функции: perimeter(10, 20) -> 60
    '''
    if isinstance(a, str) or isinstance(b, str):
        return 'Invalid input'
    if a < 0 or b < 0:
        return 'Invalid input'
    if a == 0 or b == 0:
        return "The figure doesn't exist"
    return 2 * (a + b)


