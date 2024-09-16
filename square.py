
def area(a):
    '''
    Возваращает площадь квадрата со стороной a.

        Параметры:
            a(int): десятичное число - сторона квадрата

        Возвращаемое значение:
            a * a(int): целое число - площадь квадрата

    Пример вызова функции: area(10) -> 100
    '''
    if isinstance(a, bool):
        return 'Invalid input'
    if isinstance(a, str):
        return 'Invalid input'
    if a < 0:
        return 'Invalid input'
    if a == 0:
        return "The figure doesn't exist"
    return a * a


def perimeter(a):
    '''
    Возваращает периметр квадрата со стороной a

        Параметры:
            a(int): десятичное число - сторона квадрата

        Возвращаемое значение:
            4 * a (int): целое число - периметр квадрата

    Пример вызова функции: perimeter(10) -> 40
    '''
    if isinstance(a, bool):
        return 'Invalid input'
    if isinstance(a, str):
        return 'Invalid input'
    if a < 0:
        return 'Invalid input'
    if a == 0:
        return "The figure doesn't exist"
    return 4 * a

