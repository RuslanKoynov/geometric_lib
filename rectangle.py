def area(a, b): 
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))) or a <= 0 or b <= 0:
        return -1
    return a * b

"""принимает стороны прямоугольника - возвращает площадь"""

def perimeter(a, b):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))) or a <= 0 or b <= 0:
        return -1
    return 2 * (a + b)

"""принимает стороны прямоугольника - возвращает периметр"""
