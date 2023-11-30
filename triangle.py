def is_triangle(a, b, c):
    """
    Проверяет возможность существования треугольника с соответственными сторонами
    """
    return a + b > c and a + c > b and b + c > a

def area(a, h): 
    """
    Принимает числа a и h(основание и высота треугольника), возвращает площадь треугольника
    """
    if (not(isinstance(a, int)) or not(isinstance(h, int))):
        raise TypeError("Invalid data type")
    if (a < 0 or h < 0):
        raise ValueError("Invalid value")
    return a * h / 2 

def perimeter(a, b, c): 
    """
    Принимает числа a,b и c(стороны треугольника), возвращает периметр треугольника
    """
    if (not(isinstance(a, int)) or not(isinstance(b, int)) or not(isinstance(c, int))):
        raise TypeError("Invalid data type")
    if (a < 0 or b < 0 or c < 0):
        raise ValueError("Invalid value")
    if (not(is_triangle(a, b, c))):
        raise ValueError("Invalid value")
    return a + b + c 
