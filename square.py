
def area(a):
    '''Возвращает квадратную площадь.

            Параметры:
                a (int): сторона квадрата
            Возвращает:
                (int): площадь квадрата

            Пример вызова:
                area(3) = 9
    '''

    if type(a) == str:
        return "Error: Invalid Length"

    if type(a) == float:
        return "Error: Not Integer Length"

    if a == 0:
        return "Error: Zero Length"

    if a < 0:
        return "Error: Negative Length"

    return a * a


def perimeter(a):
    '''Возвращает периметр квадрата.

            Параметры:
                a (int): сторона квадрата
            Возвращает:
                (int): периметр квадрата
            
            Пример вызова:
                area(3) = 12
    '''

    if type(a) == str:
        return "Error: Invalid Length"

    if type(a) == float:
        return "Error: Not Integer Length"

    if a == 0:
        return "Error: Zero Length"

    if a < 0:
        return "Error: Negative Length"

    return 4 * a

