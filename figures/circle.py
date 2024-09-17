import math


def area(r):
    '''Takes the value of radius r, returns the circle's area'''
    return round(math.pi * r * r, 2)


def perimeter(r):
    '''Takes the value of radius r, returns the circle's perimeter'''
    return round(2 * math.pi * r, 2)

