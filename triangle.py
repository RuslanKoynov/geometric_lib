def area(a, h):
    '''
    Функция, для вычисления площади треугольника со стороной a и высотой h.

        Параметры:
            a(int, float) - число (сторона треугольника)
            h(int, float) - число (высота треугольника)
        Возвращаемое значение:
            area(float) - площадь треугольника со стороной a и высотой h.

    Пример вызова функции:
        area(3, 4) ==> 6.0
        area(1.4, 6.78) ==> 4.7459999999999996
    '''    
    return a * h / 2

def perimeter(a, b, c):
    '''
    Функция, для вычисления периметра треугольника со сторонами a, b и c.

        Параметры:
            a,b,с(int, float) - числа (стороны треугольника)
        Возвращаемое значение:
            perimeter(int, float) - периметра треугольника со сторонами a, b и c.

    Пример вызова функции:
        perimeter(11, 4, 7) ==> 22
        perimeter(3.72, 1.34, 4.126) ==> 9.186
    '''
    return a + b + c
