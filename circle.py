import math


def area(r):
    '''
    Возвращает площадь круга радиуса r 

        Параметры:
            r (int/float): радиус круга

        Возвращаемое значение (float):
            площадь круга радиуса r по математической формуле 
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Возвращает периметр окружности радиуса r
    
        Параметры:
            r (int/float): радиус окружности
        
        Возвращаемое значение (float):
            периметр окружности радиуса r по математической формуле
    '''
    return 2 * math.pi * r

