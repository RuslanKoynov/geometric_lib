# Описание проекта

Этот проект представляет собой множество функций, которые расчитывают площадь и периметр различных геометрических фигур. 
#### Например 
- В файле rectangle.py считается площадь и периметр прямоугольника
>def area(a, b): 
    return a * b  
" вводим стороны прямоугольника, фунция возвращает площадь прямоугольника "  
> def perimeter(a, b): 
    return 2*(a + b)  
" вводим стороны прямоугольника, фунция возвращает площадь прямоугольника "
- В файле triangle.py считается площадь и периметр треугольника

>def area(a, h):   
     return a * h / 2   
" вводится длинна стороны треугольника и его высота, функция возвращает площадь треугольника "
>def perimeter(a, b, c):  
    return a + b + c     
" вводятся стороны треугольника, функция возвращает периметр треугольника "
- В файле circle.py считается площадь и периметр окружности
>import math  
def area(r): 
    return math.pi * r * r  
" вводится площадь окружности, возвращается её радиус "
>def perimeter(r): 
    return 2 * math.pi * r  
" вводится радиус окружности, возвращается её пиреметр "
- В файле square.py считается площадь и периметр окружности
>def area(a): 
    return a * a  
" принимает число a - длинну стороны квадрата, возвращает площадь этого квадрата "  
>def perimeter(a):
    return 4 * a  
" принимает число a, возвращает пириметр квадрата со стороной a "

## Описание каждой функции 
### AREA- функция, которая считает площадь.
#### Прямоугольник
```
def area(a, b):  
     return a * b
a = 5  
b = 2  
print (area(a,b)) - > 10
```
#### Треугольник
```
def area(a, h): 
    return a * h / 2 
a = 5  
h = 2.5  
print (area(a,b)) - > 12.5
```
#### Квадрат
```
def area(a): 
    return a * a 
a = 5    
print (area(a)) - > 25
```
#### Круг
```
def area(r):
    return math.pi * r * r
r = 5   
print (area(r)) - > 78.5
```


### PERIMETR- функция, которая считает периметр.
#### Прямоугольник
```
def perimeter(a, b): 
    return 2*(a + b)
a = 5  
b = 2  
print (perimeter(5, 2)) - > 20
```
#### Треугольник
```
def perimeter(a, b, c): 
   return a + b + c  
   
a = 5  
b = 4
c = 3
print (perimeter(5, 4, 3)) - > 12
```
#### Квадрат
```
def perimeter(a):
    return 4 * a
    
a = 5    
print (perimeter(5)) - > 20
```
#### Круг
```
def perimeter(r):
  return 2 * math.pi * r
  
r = 5
print (perimeter(5))=34.5
```

## История изменения проекта  

| Author       | Date       | Commit                 | Hash|
|--------------|------------|------------------------|----------|
|S0A0D0Do <anshvecova232@gmail.com>| Thu Oct 12 09:40:16 2023 +0300 | dock: add new file circle.py | 615cf8cb65b8861699e1442a70cde8cdb03ed341 |
|S0A0D0Do <anshvecova232@gmail.com>| Thu Oct 12 09:38:33 2023 +0300 | dock add new file rectangle.py | b2a6c70e87fa7c236315f00e1f9e5700c12d1731|
|S0A0D0Do <anshvecova232@gmail.com>| Thu Oct 12 09:34:57 2023 +0300 | add new file triangle.py | 0d6657542801da3ebadfa0bf21eb3633f71cf2b0|
|S0A0D0Do <anshvecova232@gmail.com>| Thu Oct 12 09:34:57 2023 +0300 | dock: add new file square.py| d8ce79c43181a27ba920969080319bda464bd690|
|S0A0D0Do <anshvecova232@gmail.com>| Thu Oct 12 03:31:29 2023 +0300 | add new comments in py fails| cfe3e172e79ae898445f64433bfdd7dd35c5ba45 |
|