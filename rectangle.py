
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

    return 2 * (a + b)