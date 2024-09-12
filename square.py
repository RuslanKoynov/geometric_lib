def area(a):
    #Accepts side of square a and returns the area of square#
    if (type(a) == str or a < 0):
        return False
    
    return a * a


def perimeter(a):
    #Accepts side of square a and returns the perimeter of square#
    if (type(a) == str or a < 0):
        return False
    
    return 4 * a
