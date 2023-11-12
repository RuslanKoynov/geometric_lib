def area(a,h):
    # принимает сторону(a) треугольника и высоту (h) , возращает его площадь (a умноженное на поливину h)
    if (type(a) == type(1)) and (type(h) == type(1)):
        if a >= 0 and h >= 0:
            return a * h * 0.5
        return "Argumeng cant be <0"
    else:
        return "Wrong argument-type"

def perimeter(a,b,c):
    # принимает три стороны(a,b,c) треугольника, возращает его периметр (a + b + c)
    if (type(a) == type(1)) and (type(b) == type(1)) and (type(c) == type(1)):
        if a > 0 and b > 0 and c > 0:
            return a + b + c
        if a == 0 and a == b and c == 0:
            return 0
        return "Argumeng cant be <0 or if one arg = 0 other must be 0"
    else:
        return "Wrong argument-type"
