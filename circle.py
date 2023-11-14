import math
print('Введите радиус r: ')
r=int(input())
def area(r):
    return math.pi * r * r


def perimeter(r):
    return 2 * math.pi * r

print('площадь равна', area(r))
print('периметр равен ', perimeter(r))
