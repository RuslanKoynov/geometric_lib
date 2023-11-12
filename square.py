
def area(a):
    # принимает сторону(a) квадрата - число, возращает его площадь (a в квадрате) 
    if type(a) == type(1):
        if a >= 0:
            return a*a
        return "Argumeng cant be <0"
    else:
        return "Wrong argument-type"


def perimeter(a):
    # принимает сторону(a) квадрата - число, возращает его периметр (a умноженное на 4)
    if type(a) == type(1):
        if a >= 0:
            return a*4
        return "Argumeng cant be <0"
    else:
        return "Wrong argument-type"
