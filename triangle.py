def area(a, h):
    #Accepts side and height of triangle a, h
    #and returns the area of triangle#
    if (type(a) == str or type(h) == str or a < 0 or h < 0):
        return False
    
    return (a * h) / 2 

def perimeter(a, b, c):
    
    #Accepts sides of triangle a,b,c
    #and returns the perimeter of triangle#
    if (type(a) == str or type(b) == str or type(c) == str or \
        a < 0 or b < 0 or c < 0):
        return False
    
    return a + b + c
