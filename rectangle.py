def area(a,b):
    # получает стороны(a,b) прямоугольника - 2 чилса,возращает его площадь (a умноженное на b)
    if (type(a) == type(1)) and (type(b) == type(1)):
        if a >= 0 and b >= 0:
            return a * b
        return "Argumeng cant be <0"
    else:
        return "Wrong argument-type"

def perimeter(a,b):
    # получает стороны (a,b) прямоугольника - 2 числа, возращает его периметр (сумма a и b, умноженное на 2)
    if (type(a) == type(1)) and (type(b) == type(1)):
        if a > 0 and b > 0:
            return (a + b) * 2
        if a == 0 and a == b:
            return 0
        return "Argumeng cant be <0 or only one be 0"
    else:
        return "Wrong argument-type"
