print('введите сторону треугольника a: ')
a=int(input())
print('введите сторону треугольника b: ')
b=int(input())
print('введите сторону треугольника c: ')
c=int(input())
print('введите высоту треугольника h: ')
h=int(input())
def area(a, h): 
    return a * h / 2 

def perimeter(a, b, c): 
    return a + b + c
print('площадь равна ', area(a,h))
print('периметр равен ', perimeter(a,b,c))
