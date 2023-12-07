# Math library
Library for calculation of area and perimeter of circles, rectangles, squares, and triangles.

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

# Docs
## Circles
**area(r)**
Calculates and returns area of a circle with radius `r`.
*Arguments:*
- `r` --- radius of the circle

*Returns:* area of the circle
*Example:*
```
>>> area(2)
12.566370614359172
```

**perimeter(r)**
Calculates perimeter/length of the circle with radius `r`.
*Arguments:*
- `r` --- radius of the circle

*Returns:* perimeter/length of the circle
*Example:*
```
>>> perimeter(1)
6.283185307179586
```

## Rectangle
**area(a, b)**
Calculates and returns area of a rectangle with sides `a`, and `b`.
*Arguments:*
- `a`, `b` --- sides of the rectangle

*Returns:* area of the rectangle
*Example:*
```
>>> area(3, 4)
12
```

**perimeter(a, b)**
Calculates perimeter of the rectangle with sides `a`, and `b`.
*Arguments:*
- `a`, `b` --- sides of the rectangle

*Returns:* perimeter of the rectangle
*Example:*
```
>>> perimeter(3, 4)
14
```

## Square
**area(a)**
Calculates and returns area of a square with side `a`.
*Arguments:*
- `a` --- side of the square

*Returns:* area of the square
*Example:*
```
>>> area(3)
9
```

**perimeter(a)**
Calculates perimeter of the square with side `a`.
*Arguments:*
- `a` --- side of the square

*Returns:* perimeter of the square
*Example:*
```
>>> perimeter(3)
18
```

## Triangle
**area(a, h)**
Calculates and returns area of a triangle where `a` is the length of the base of the triangle, and `h` is the height.
*Arguments:*
- `a` --- length of the base of the triangle
- `h` --- height of the triangle

*Returns:* area of the triangle
*Example:*
```
>>> area(4, 3)
6.0
```

**perimeter(a, b, c)**
Calculates perimeter of the triangle with sides `a`, `b`, and `c`.
*Arguments:*
- `a`, `b`, `c` --- sides of the triangle

*Returns:* perimeter of the triangle
*Example:*
```
>>> perimeter(3, 4, 5)
12
```

# Tests
Autotests success: 14/24 (58.3%)

# Commit history
|Commit|Message|
|------|-------|
|8ba9aeb|L-03: Circle and square added|
|d078c8d|L-03: Docs added|
|a6f3fc1|Add rectangle area/perimeter calculation|
|6324d5a|Add triangle area/perimeter calculation; fix rectangle calc|
|098fa2d|docs: add circle.py docs|
|f47784c|docs: add rectangle.py docs|
|d57a2b4|docs: add square.py docs|
|152fc05|docs: add triangle.py docs|
|f10a895|test: add tests for functions area and perimeter in rectangle.py, circle.py, square.py, triangle.py|
|bc2b44d|docs: add new commit in README.md's commit table|
|238f18b|test: add tests for incorrect (negative) input values in all modules|
|3e14352|docs: update commit table with latest commits|
|5c1781c|docs: add autotests success value; update commit table|
|12d676b|test: fix copy-pasted method name|
