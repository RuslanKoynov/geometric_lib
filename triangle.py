
def area(a, h): 
    '''Возвращает площадь треугольника.

            Параметры:
                a (int): основание треугольника
                h (int): высота треугольника
            Возвращает:
                (int): площадь треугольника

            Пример вызова:
                area(5, 4) = 10
    '''

    if type(a) == str or type(h) == str:
        return "Error: Invalid Length"

    if type(a) == float or type(h) == float:
        return "Error: Not Integer Length"

    if (a == 0) or (h == 0):
        return "Error: Zero Length"

    if (a < 0) or (h < 0):
        return "Error: Negative Length"

    return a * h / 2


def perimeter(a, b, c):
    '''Возвращает периметр треугольника.

            Параметры:
                a (int): первая сторона треугольника
                b (int): вторая сторона треугольника
                c (int): третья сторона треугольника
            Возвращает:
                (int): периметр треугольника

            Пример вызова:
                area(3, 2, 3) = 8
    '''

    if type(a) == str or type(b) == str or type(c) == str:
        return "Error: Invalid Length"

    if type(a) == float or type(b) == float or type(c) == float:
        return "Error: Not Integer Length"

    if (a == 0) or (b == 0) or (c == 0):
        return "Error: Zero Length"

    if (a < 0) or (b < 0) or (c < 0):
        return "Error: Negative Length"

    return a + b + c 