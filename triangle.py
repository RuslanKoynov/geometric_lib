

def area(a, h):
    """
    Возвращает площадь треугольника

        Параметры:
            a (float): длина стороны треугольника
            h (float): длина высоты прилегающей к стороне треугольника a

        Возвращаемое значение:
            area (float): площадь треугольника
    """
    return a * h / 2


def perimeter(a, b, c):
    """
    Возвращает периметр треугольника

        Параметры:
            a (float): длина первой стороны треугольника
            b (float): длина второй стороны треугольника
            c (float): длина третьей стороны треугольника

        Возвращаемое значение:
            area (float): периметр треугольника
    """
    return a + b + c
