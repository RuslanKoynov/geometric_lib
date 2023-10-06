def area(a, h):
    '''
    Реализует подсчёт площади треугольника со стороной a, и высотой, опущенной на эту сторону h

        Параметры:
            a (int, float, etc) : длина стороны треугольника
            h (int, float, etc) : длина высоты треугольника, опущенной на эту сторону

        Возвращаемое значение:
            area (int, float, etc) : площадь данного треугольника
    '''
    return a * h / 2 

def perimeter(a, b, c):
    '''
    Реализует нахождение периметра для треугольника со сторонами a, b, c

        Параметры:
            a, b, c (int, float, etc) : соответственные стороны треугольника

        Возвращаемое значение:
            perimeter (int, float, etc) : периметр треугольника
    '''
    return a + b + c 