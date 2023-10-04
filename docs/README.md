# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

## Circle
### 1. Area

```
area(r)
```
 The area(r) function calculates the area of ​​a circle with radius.

Formula:

     Area = π * r^2

Description:
- `Area` is the area of the circle.
- `π` (pi) is a mathematical constant approximately equal to 3.14159.
- `r` is the radius of the circle
  
```python
 def area(r):  
    return math.pi * r * r
```
Example of using:
```python
from circle import area as circle_area_def

radius = 5.0
circle_area = circle_area_def(radius)
print(circle_area)
```
### 2. Perimeter

```
perimeter(r)
```
 The perimeter(r) function calculates the perimeter of a circle. 


Formula:

     Perimeter = 2 * π * r

Description:
- `Perimeter`is the perimeter of the circle.
- `π` (pi) is a mathematical constant approximately equal to 3.14159.
- `r` is the radius of the circle.
  
```python
 def perimeter(r): 
    return 2 * math.pi * r
```
Example of using:

```python
from circle import perimeter as circle_perimeter_def

radius = 5.0
circle_perimeter = circle_perimeter_def(radius)
print(circle_perimeter)
```


## Rectangle

### 1. Area

```
area(a, b)
```
  The area(a, b) function calculates the area of a rectangle.

Formula:

     Area = a * b

Description:
- `Area` is the area of the rectangle.
- `a` is the length of one side of the rectangle.
- `b` is the length of the other side of the rectangle.
  
```python
def area(a, b):
    return a * b
```
Example of using:

```python
from rectangle import area as rectangle_area_def

a, b = 5, 10
rectangle_area = rectangle_area_def(a, b)
print(rectangle_area)
```
### 2. Perimeter

```
perimeter(a, b)
```
The perimeter(a, b) function calculates the perimeter of a rectangle.

Formula:

     Perimeter = 2 * (a + b)

Description:
- `Perimeter` is the perimeter of the rectangle.
- `a` is the length of one side of the rectangle.
- `b` is the length of the other side of the rectangle.
    '''
  
```python
def perimeter(a, b):
    return 2 * (a + b)
```
Example of using:
```python
from rectangle import perimeter as rectangle_perimeter_def

a, b = 5, 10
rectangle_perimeter = rectangle_perimeter_def(a, b)
print(rectangle_perimeter)
```
## Square

### 1. Area

```
area(a)
```
The area(a) function calculates the area of a square.

Formula:

     Area = a * a

Description:
- `Area` is the area of the square.
- `a` is the length of one side of the square.
  
```python
def area(a):
    return a * a
```

Example of using:
```python
 from square import area as square_area_def

a = 10
square_area = square_area_def(a)
print(square_area)

```
### 2. Perimeter

```
perimeter(a)
```
The perimeter(a) function calculates the perimeter of a square.

Formula:

     Perimeter = 4 * a

Description:
- `Perimeter` is the perimeter of the square.
-  `a` is the length of one side of the square.
    '''
  
```python
def perimeter(a):
    return 4 * a
```
Example of using:
```python
from square import perimeter as square_perimeter_def

a = 10
square_perimeter = square_perimeter_def(a)
print(square_perimeter)
```
## Commits hash:
```
commit 9c4e31a1308e8919cad100db77ed60f1c6fb9bbb (HEAD -> main)
Author: Лимарев Егор <limarevegor@MacBook-Air-Limarev.local>
Date:   Wed Sep 20 14:28:54 2023 +0300

    delite file

commit 585f88e53d3a5bcbce5b530bf15bf69d3a9a1b46 (origin/main, origin/HEAD, test_1)
Author: Лимарев Егор <limarevegor@MacBook-Air-Limarev.local>
Date:   Mon Sep 11 03:26:15 2023 +0300

    fixed error in file

commit 14ba8a8ab57fbb62b847c0a0d870f7012f4c0926
Author: Лимарев Егор <limarevegor@MacBook-Air-Limarev.local>
Date:   Mon Sep 11 03:20:31 2023 +0300

    add new file

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square added
```











