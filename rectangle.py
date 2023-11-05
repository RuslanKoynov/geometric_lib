
def area(a, b):
    '''Возвращает площадь прямоугольника.

            Параметры:
                a (int): first side of the rectangle
                b (int): second side og the rectangle
            Возврат:
                (int): area of the rectangle

            Пример вызова:
                area(3, 2) = 6
    '''

    if type(a) == str or type(b) == str:
        return "Error: Invalid Length"

    if type(a) == float or type(b) == float:
        return "Error: Not Integer Length"

    if (a == 0) or (b == 0):
        return "Error: Zero Length"

    if (a < 0) or (b < 0):
        return "Error: Negative Length"

    return a * b 


def perimeter(a, b):
    '''Возвращает периметр прямоугольника.

            Параметры:
                a (int): первая сторона прямоугольника
                b (int): вторая сторона прямоугольника.
            Возврат:
                (int): периметр прямоугольника

            Пример вызова:
                perimeter(3, 2) = 10
    '''

    if type(a) == str or type(b) == str:
        return "Error: Invalid Length"

    if type(a) == float or type(b) == float:
        return "Error: Not Integer Length"

    if (a == 0) or (b == 0):
        return "Error: Zero Length"

    if (a < 0) or (b < 0):
        return "Error: Negative Length"

    return 2 * (a + b)