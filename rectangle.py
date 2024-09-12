def area(a, b):
    #Accepts sides of rectangle a,b and returns the area of rectangle#
    if (type(a) == str or type(b) == str or a < 0 or b < 0):
        return False
    
    return a * b 

def perimeter(a, b):
    #Accepts sides of rectangle a,b and returns the perimeter of rectangle#
    if (type(a) == str or type(b) == str or a < 0 or b < 0):
        return False
    
    return 2*(a + b)
