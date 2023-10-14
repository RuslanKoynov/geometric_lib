# Library Documentation

The library is designed to count the areas and perimeters
of various geometric shapes, such as :
`circle, rectangle, square, triangle`

All calculations are made via these formulas:
- Circle: S = πR²
- Circle: P = 2πR
- Rectangle: S = ab
- Rectangle: P = 2a + 2b
- Square: S = a²
- Square: P = 4a

## Functions
### Circle

***file***  *geometric_lib.**circle.py***\
\
**area(r)**\
calculate circle area
```
Parameters:
    r (int) - radius
```
```
Returns:
    area (int) - circle area
```
\
**perimeter(r)**\
calculate circle perimeter
```
Parameters: 
    r (int) - radius
```
```
Returns: 
    perimetr (int) - circle perimetr
```

### Rectangle

***file***  *geometric_lib.**rectangle.py***\
\
**area(a, b)**\
calculate rectangle area
```
Parameters:
    a (int) - rectangle side
    b (int) - rectangle side
```
```
Returns: 
    area (int) - rectangle area
```
\
**perimeter(a, b)**\
calculate rectangle perimeter
```
Parameters: 
    a (int) - rectangle side
    b (int) - rectangle side
```
```
Returns: 
    perimetr (int) - rectangle perimeter
```

## Square

***file***  *geometric_lib.**square.py***\
\
**area(a)**\
calculate square area
```
Parameters:
    a (int) - square side
```
```
Returns: 
    area (int) - square area
```
\
**perimeter(r)**\
calculate square perimeter
```
Parameters: 
    a (int) - sqaure side
```
```
Returns: 
    perimetr (int) - square perimeter
```

## Triangle

***file***  *geometric_lib.**triangle.py***\
\
**area(a, h)**\
calculate triangle area
```
Parameters:
    a (int) - triangle base side
    h (int) - triangle height to base side
```
```
Returns: 
    area (int) - triangle area
```
\
**perimeter(a, b, c)**\
calculate triangle perimeter
```
Parameters: 
    a (int) - triangle side
    b (int) - triangle side
    c (int) - triangle side
```
```
Returns: 
    perimetr (int) - triangle perimeter
```

## Project commit history
|  Commit | Message   |
|--------:|-----------|
|       1 | Javascript |
|       2 | Python    |
|       3 | SQL       |