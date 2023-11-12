import math


def area(r):
    # принимает радиус круга(r), возрашает его площадь (pi умноженное на r в квадрате)
    if type(r) == type(1):
        if r >= 0:
            return math.pi * r * r
        return "Argumeng cant be <0"
    else:
        return "Wrong argument-type"


def perimeter(r):
    # принимает радиус круга(r), возращает его периметр (pi умноженное на r и умноженное на 2)
    if type(r) == type(1):
        if r >= 0:
            return 2 * math.pi * r
        return "Argumeng cant be <0"
    else:
        return "Wrong argument-type"
