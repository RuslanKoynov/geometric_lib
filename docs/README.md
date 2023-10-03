# Math formulas

## General description of the project:

**This project contains 4 files, each of which contains two functions for calculating the perimeter and area of ​​geometric shapes (triangle, square, circle and rectangle). All functiouns are written in Python.**

## Area

- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter

- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

---

##Description of each function:

- _Rectangles functions:_

```python
def area(a, b):
    return a * b
'''Takes two numbers: a and b.
    Returns the area of ​​the rectangle with these parameters.'''
```

**Example call:**

```python
print(area(2, 4))
```

**Example output:**

```python
8
```

<br>
<br>

```python
def perimeter(a, b):
    return a * b
'''Takes two numbers: a and b. Returns the perimeter of ​​the rectangle with these parameters'''
```

**Example call:**

```python
print(perimeter(2, 4))
```

**Example output:**

```python
12
```

<br>
<br>
<br>
<br>

- _Triangles functions:_

```python
def area(a, h):
    return a * h / 2
'''Takes two numbers: a and h - the base and height of the triangle.
Returns the perimeter of the triangle with these parameters.'''
```

**Example call:**

```python
print(area(2, 4))
```

**Example output:**

```python
8
```

<br>
<br>

```python
def perimeter(a, b, c):
    return a * b
'''Takes three numbers: a, b, c - sides of the triangle.
Returns the perimeter of a triangle with these parameters'''
```

**Example call:**

```python
print(perimeter(2, 2, 2))
```

**Example output:**

```python
6
```

<br>
<br>
<br>
<br>

- _Squares functions:_

```python
def area(r):
    return a * a
'''Takes one number: a - side of the square.
    Returns the area of ​​a square with this value.'''
```

**Example call:**

```python
print(area(12))
```

**Example output:**

```python
144
```

<br>
<br>

```python
def perimeter(a):
    return 4 * a
'''Takes one value: a - side of the square.
    Returns the perimeter of such a square with this value.'''
```

**Example call:**

```python
print(perimeter(8))
```

**Example output:**

```python
32
```

<br>
<br>
<br>
<br>

- _Circles functions:_

```python
import math

def area(r):
    return math.pi * r * r
'''Takes one value: r - radius of the circle.
    Returns the area of ​​a circle with this radius'''
```

**Example call:**

```python
print(area(4))
```

**Example output:**

```python
50.26548245743669
```

<br>
<br>

```python
import math

def perimeter(r):
    return 2 * math.pi * r
'''Takes one value: r - radius of the circle.
    Returns the perimiter of ​​a circle with this radius'''
```

**Example call:**

```python
print(perimeter(3))
```

**Example output:**

```python
18.84955592153876
```

---

##Project change history:
| Hash | Date | Author | Comment |  
|:------------------------------|:-----------------------------:|------------------------------:|:--------------------------|
| 8ba9aeb3ce | Thu Mar 4 14:54:08 2021 | smartiqa <info@smartiqa.ru> | Circle and square added |
| d078c8d9ee | Thu Mar 4 14:55:29 2021 | smartiqa <info@smartiqa.ru> | Docs added |
| aab72bf42b | Mon Sep 11 17:02:20 2023 | Iosif <osya.amer@gmail.com> | Added new file |
| dc012b6271 | Mon Sep 11 17:02:20 2023 | Iosif <osya.amer@gmail.com> | Error was fixed |
| 497b906dd6 | Mon Oct 2 15:15:59 2023 | Iosif <osya.amer@gmail.com> | docs: Added comments for all project functions|
