
def area(a):
    if not isinstance(a, (int, float)) or a <= 0:
        return -1
    return a * a

"""принимает сторону квадрата - возвращает площадь"""

def perimeter(a):
    if not isinstance(a, (int, float)) or a <= 0:
        return -1
    return 4 * a

"""принимает сторону квадрата - возвращает периметр """


