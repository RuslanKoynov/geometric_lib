# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

# Functions 
## Circle
`area` function takes value r and returns it's square value multiplied on pi
```python
def area(r):
    return math.pi * r * r
```

`perimeter` function takes value r and multiplies it on 2 and pi
```python
def perimeter(r):
    return 2 * math.pi * r
```

## Rectangle
`area` function takes values a and b and returns result of their multiplication
```python
def area(a, b):
    return a * b
```

`perimeter` function takes values a and b and returns result of their multiplication
```python
def perimeter(a, b):
    return a * b
```

## Square
`area` function takes value a and returns it's square value
```python
def area(a):
    return a * a
```
`perimeter` function takes value a and returns it's value multiplied by 4
```python
def perimeter(a):
    return 4 * a
```

## Triangle
`area` function takes values of a and h and returns result of their mupltiplication divided by 2
```python
def perimeter(a, h):
    return a * h / 2
```
`perimeter` function takes values a, b, c and returns their sum
```python
def perimeter(a, b, c):
    return a + b + c
```

# Commits
| Author | Hash | Date | Commentary |
| --- | --- | --- | --- |
| Denis Gapilov <124xyz@mail.ru> | 960b238c26f7de9fc50eb8a7f4bed9c80dd43d4a | Sun Sep 17 02:32:40 2023 +0300 | fix: perimeter calculation in rectangle.py |
| Denis Gapilov <124xyz@mail.ru> | 39fb6ff8e1adbee09cb8b57c14bc0be298d67d5e | Sun Sep 17 02:21:05 2023 +0300 | feat: created file rectangle.py |
| smartiqa <info@smartiqa.ru> | d078c8d9ee6155f3cb0e577d28d337b791de28e2 | Thu Mar 4 14:55:29 2021 +0300 | L-03: Docs added |
| smartiqa <info@smartiqa.ru> | 8ba9aeb3cea847b63a91ac378a2a6db758682460 | Thu Mar 4 14:54:08 2021 +0300 | L-03: Circle and square added |