import math


def area(r):
    '''Возвращает площадь круга.

            Параметры:
                r (int): радиус круга
            Возврат:
                (float): площадь круга

            Пример вызова:
                area(3) = 28.274333882308138
    '''
    
    if type(r) == str:
        return "Error: Invalid Length"

    if type(r) == float:
        return "Error: Not Integer Length"

    if r == 0:
        return "Error: Zero Length"

    if r < 0:
        return "Error: Negative Length"

    return math.pi * r * r


def perimeter(r):
    '''Возвращает периметр круга.

            Параметры:
                r (int): радиус круга
            Возврат:
                (плавающее): периметр круга

            Пример вызова:
                perimeter(3) = 18.84955592153876
    '''

    if type(r) == str:
        return "Error: Invalid Length"

    if type(r) == float:
        return "Error: Not Integer Length"

    if r == 0:
        return "Error: Zero Length"

    if r < 0:
        return "Error: Negative Length"

    return 2 * math.pi * r

