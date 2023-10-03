# Math formulas

## Area

- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ah/2


## Perimeter

- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c


## **PROGRAMS**

# cirqule

```python
import math

def area(r):
    '''
    принимает значение радиуса r, возвращает значение площади круга
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    принимает значение радиуса r, возвращает значение периметра кругa
    '''
    return 2 * math.pi * rdef
```

## example

```python
r = 5
print('area =', area(r), ';perimetr =', perimeter(r)) 
```

```
area = 78.53981633974483; perimeter = 31.41592653589793
```

## Rectangle

```python
def area(a, b):
     '''
     принимает знвчения сторон прямоугольника a и b, возвращает занчение площади
     '''
     return a * b
def perimeter(a, b):
     '''
     принимает знвчения сторон прямоугольника a и b, возвращает занчение периметра
     '''
     return 2 * (a + b)
```

## example

```python
a = 10
b = 5
print('area =', area(a,b), ';perimetr =', perimeter(a,b))
```

```
area = 50; perimeter = 30
```


## Triangle

```python
def area(a, h):
     '''
     принимает значения сороны теугольника a и провеенной к  ней высоте h, возвращает значение площади треугольника
     '''
     return a * h / 2
def perimeter(a, b, c):
     '''
     принимает значение всех сторон треугольника, возвращает значение периметра
     '''
     return a + b + c
```

## example

```python

a = 4
h = 2
b = 2.2
c = 3.6
print('area =', area(a,h), '; perimeter =', perimeter(a,b,c))
```

```
area = 4; perimeter = 9.8
```

## Square

```python
def area(a):
    '''
    принимает значение стороны квадрата, возвращает значение его площади
    '''
    return a * a


def perimeter(a):
    '''
    принимает значение периметра квадрата, возвращает значение его периметра
    '''
    return 4 * a

```

## example

```python
a = 2
print('area =', area(a), ';perimeter =', perimeter(a))
```

```
area = 4; perimeter = 8
```

# commits

```bash
commit 6012966f0cbf11ab65609409dac6ab1f1faa4711
Author: Ekaterina Bochagova <ekaterina.bochagova@yandex.ru>
Date:   Fri Sep 15 13:37:59 2023 +0300

    bug fixed

commit 97b6d4afdb89b1d84f264ed3a9d2f8da9df45420
Author: Ekaterina Bochagova <ekaterina.bochagova@yandex.ru>
Date:   Fri Sep 15 13:35:39 2023 +0300

    rectangle.py added

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square added

```
