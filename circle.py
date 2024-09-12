import math
    #Import library math for pi value#

def area(r):
    #Accepts radius of circle r and returns the area of circle#
    if (type(r) == str or r < 0):
        return False
    
    return math.pi * r * r


def perimeter(r):
    #Accepts radius of circle r and returns the perimeter of circle#
    if (type(r) == str or r < 0):
        return False
    
    return 2 * math.pi * r
