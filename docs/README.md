# Math formulas

##General discription
**There are four files that include finding the area and perimeter of various geometric shapes (circle, rectangle, square and triangle), the programs are written in Python.**

## Area

- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter

- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

---

##Discriprion of each function

* **Circle function**

Area

```python
import math

def area(r):
    return math.pi * r * r
'''Takes one number r - radius of the circle.
    Returns the area of ​​a circle with this r'''
```

**Example call:**

```python
print(area(2))
```

**Example output:**

```python
12.566370614359172
```

Perimeter

```python
import math

def perimeter(r):
    return 2 * math.pi * r
'''Takes one number r - radius of the circle.
    Returns the perimiter of ​​a circle with this r'''
```

**Example call:**

```python
print(perimeter(2))
```

**Example output:**

```python
12.566370614359172
```

* **Rectangle functions**

Area

```python
def area(a, b):
    return a * b
'''Takes two numbers a and b.
    Returns the area of ​​the rectangle with these a and b'''
```

**Example call:**

```python
print(area(1, 2))
```

**Example output:**

```python
2
```

Perimeter

```python
def perimeter(a, b):
    return a * b
'''Takes two numbers: a and b 
    Returns the perimeter of ​​the rectangle with these a and b'''
```

**Example call:**

```python
print(perimeter(2, 3))
```

**Example output:**

```python
10
```

* **Triangles functions**

Area

```python
def area(a, h):
    return a * h / 2
'''Takes two numbers a and h - the base and height of the triangle.
Returns the perimeter of the triangle with these a and h'''
```

**Example call:**

```python
print(area(1, 2))
```

**Example output:**

```python
1.0
```

Perimeter

```python
def perimeter(a, b, c):
    return a + b + c
'''Takes three numbers a, b, c - sides of the triangle.
Returns the perimeter of a triangle with these a, b and c'''
```

**Example call:**

```python
print(perimeter(1, 3, 4))
```

**Example output:**

```python
8
```

* **Squares functions**

Area


```python
def area(r):
    return a * a
'''Takes one number a - side of the square.
    Returns the area of ​​a square with this a'''
```

**Example call:**

```python
print(area(2))
```

**Example output:**

```python
4
```

Perimeter

```python
def perimeter(a):
    return 4 * a
'''Takes one number a - side of the square.
    Returns the perimeter of such a square with this a'''
```

**Example call:**

```python
print(perimeter(2))
```

**Example output:**

```python
8
```
##Project change history:
| Hash | Date | Author | Comment |  
|:------------------------------|:-----------------------------:|------------------------------:|:--------------------------|
| 8ba9aeb3ce | Thu Mar 4 14:54:08 2021 | smartiqa <info@smartiqa.ru> | Circle and square added |
| d078c8d9ee | Thu Mar 4 14:55:29 2021 | smartiqa <info@smartiqa.ru> | Docs added |
| e4f3684a5 | Wed Sep 13 12:24:40 2023 | Sandra Min <minsandra81@gmail.com> | new file added |
| 2a931293d | Wed Sep 13 12:26:04 2023 | Sandra Min <minsandra81@gmail.com> | bug has been fixed |
| f46c99026a | Mon Oct 2 16:06:11 2023 | Sandra Min <minsandra81@gmail.com> | docs: comments has been added|
| f1ab5c4c80 | Thu Nov 16 00:38:18 2023 | Sandra Min <minsandra81@gmail.com> | test: added unittets|
| 513725a076 | Thu Nov 16 00:59:31 2023 | Sandra Min <minsandra81@gmail.com> |  test: unittests updated|
| 480cb520d1 | Thu Nov 16 03:13:57 2023 | Sandra Min <minsandra81@gmail.com> |   merge: merged with documentation_409137|

#Tests success rate

Test success: x/n(p%).
x - successfully passed tests.
n - total tests.
p - per sent of success rating.

x = 40
n = 56
p = 71%

Tests included big and small numbers, null, string and float value. 

Verdict: All the failed tests included non-int type or negative value. So, these functions can't check the type of value user inputs.


