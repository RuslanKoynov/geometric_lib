def area(a, h): 
    if not (isinstance(a, (int, float)) and isinstance(h, (int, float))) or a <= 0 or h <= 0:
        return -1
    return a * h / 2

"""принимает основание и высоту треугольника - возвращает площадь"""

def perimeter(a, b, c):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))) or a <= 0 or b <= 0 or c <= 0:
        return -1
    return a + b + c

"""принимает три стороны треугольника - возвращает периметр"""
