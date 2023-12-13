def area(a, b): 
    """
    Принимает числа a и b(стороны прямоугольника), возвращает площадь прямоугольника
    """
    if (not(isinstance(a, int)) or not(isinstance(b, int))):
        raise TypeError("Invalid data type")
    if (a < 0 or b < 0):
        raise ValueError("Invalid value")
    return a * b 

def perimeter(a, b): 
    """
    Принимает числа a и b(стороны прямоугольника), возвращает периметр прямоугольника
    """
    if (not(isinstance(a, int)) or not(isinstance(b, int))):
        raise TypeError("Invalid data type")
    if (a < 0 or b < 0):
        raise ValueError("Invalid value")
    return (a + b)*2 
