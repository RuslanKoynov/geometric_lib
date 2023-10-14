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

# Functions
## Circle

***file***  *geometric_lib.**circle.py***\
\
**area(r)**\
Calculate circle area
```
Parameters:
    r (int) - radius
```
```
Returns:
    area (float) - circle area
```
Example:
```
area(3)
>>> 28,26 
```
\
**perimeter(r)**\
Calculate circle perimeter
```
Parameters: 
    r (int) - radius
```
```
Returns: 
    perimetr (float~~~~) - circle perimetr
```
Example:
```
perimeter(3)
>>> 18,84
```

## Rectangle

***file***  *geometric_lib.**rectangle.py***\
\
**area(a, b)**\
Calculate rectangle area
```
Parameters:
    a (int) - rectangle side
    b (int) - rectangle side
```
```
Returns: 
    area (int) - rectangle area
```
Example:
```
area(2, 3)
>>> 6 
```
\
**perimeter(a, b)**\
Calculate rectangle perimeter
```
Parameters: 
    a (int) - rectangle side
    b (int) - rectangle side
```
```
Returns: 
    perimetr (int) - rectangle perimeter
```
Example:
```
perimeter(2, 3)
>>> 10
```

## Square

***file***  *geometric_lib.**square.py***\
\
**area(a)**\
Calculate square area
```
Parameters:
    a (int) - square side
```
```
Returns: 
    area (int) - square area
```
Example:
```
area(3)
>>> 9 
```
\
**perimeter(a)**\
Calculate square perimeter
```
Parameters: 
    a (int) - sqaure side
```
```
Returns: 
    perimetr (int) - square perimeter
```
Example:
```
perimeter(5)
>>> 20 
```

## Triangle

***file***  *geometric_lib.**triangle.py***\
\
**area(a, h)**\
Calculate triangle area
```
Parameters:
    a (int) - triangle base side
    h (int) - triangle height to base side
```
```
Returns: 
    area (int) - triangle area
```
Example:
```
area(2, 3)
>>> 3 
```
\
**perimeter(a, b, c)**\
Calculate triangle perimeter
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
Example:
```
perimeter(3, 4, 5)
>>> 12 
```


## Project commit history
|  Commit | Type | Message                                                    |
|--------:|------|------------------------------------------------------------|
| 8ba9aeb | L-03 | Circle and square added                                    |
| d078c8d | L-03 | Docs added                                                 |
| 7efe112 | feat | add rectangle.py                                           |
| 73ff689 | fix  | correct perimeter calculation error                        |
| c1e0b6a | docs | add functions declaration                                  |
| 249df46 | docs | add functions declaration                                  |
| c40a165 | docs | fix functions declaration text                             |
| 79e0402 | docs | add functions declaration                                  |
| 9622c94 | docs | add functions declaration                                  |
| 065024e | docs | delete old docs catalog                                    |
| 3af71cb | docs | add docs catalog, add docs/README.md file, write README.md |
| b40281a | docs | done README.md                                             |
| 87a8628 | docs | fix function declaration                                   |