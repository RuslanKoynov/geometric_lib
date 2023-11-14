print('введите сторону a')
a=int(input())
print('введите сторону b')
b=int(input())
def area(a, b): 
    return a * b 

def perimeter(a, b): 
    return (a + b)*2
print('площадь равна ',area(a,b))
print('периметр равен', perimeter(a,b))
