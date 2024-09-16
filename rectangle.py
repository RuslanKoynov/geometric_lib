def area (a, b):
    '''
    принимает значения длин сторон прямоугольника, возвращает значение площади
    '''
    return a * b

def perimeter(a, b):
    '''
    принимает значения длин сторон прямоугольника, возвращает значение периметра
    '''
    return 2 * (a + b)


print(area(1))
print(area(123456789))
print(area(True))
print(perimeter(1))
print(perimeter(123456789))
print(perimeter(True))