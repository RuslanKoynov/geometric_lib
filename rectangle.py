def area(a, b): 
    '''
    Calculates the area of rectangle
    :param a: size of the side of the rectangle (first side)
    :type a: int or float
    :param b: size of the side of the rectangle (adjacent to the first side)
    :type b: int or float
    :rtype: int or float
    :return: a*b - area of the rectangle
    :example: area(2, 4) = 8
    '''
    return a * b 

def perimeter(a, b): 
    '''
    Calculates the perimeter of rectangle
    :param a: size of the side of the rectangle (first side)
    :type a: int or float
    :param b: size of the side of the rectangle (adjacent to the first side)
    :type b: int or float
    :rtype: int or float
    :return: 2*(a+b) - perimeter of the rectangle
    example: perimeter(2, 4) = 12
    '''
    return 2*(a + b) 
