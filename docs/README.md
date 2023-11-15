# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- R ectangle: P = 2a + 2b
- Square: P = 4a

# Function
## Circle
Функция 'Area' принимает на вход значение радиуса круга и выводит значение площади круга.
```
def area(r):
    return math.pi * r * r
```

Функция 'Perimeter' принимает на вход значение радиуса круга и выводит значение площади круга.
```
def perimeter(r):
    return 2 * math.pi * r
```

## Square
Функция 'Area' принимает на вход значение стороны квадрата и выводит значение площади квадрата.
```
def area(a):
    return a * a
```

Функция 'Perimeter' принимает на вход значение стороны квадрата и выводит значение периметра квадрата.
```
def perimeter(r):
    return 2 * math.pi * r
```

### Rectangle
Функция 'Area' принимает на вход значение сторон прямоугольника и выводит значение площади прямоугольника.
```
def area(a,b):
    return a * b
```

Функция 'Perimeter' принимает на вход значение сторон прямоугольника и выводит значение периметра прямоугольника.
```
def perimeter(a,b):
    return (a + b)*2
```

## UnitTest
#### Rectangle.py
###### Correct tests
- area()
- ~~~
  input: 4,6
  output: 24
  ~~~
  ~~~
  input: 4.4, 6.6
  output: 29,04
  ~~~
  ~~~
  input: 4,0
  output: 0
  ~~~
  ###### Incorrect tests
- ~~~
  input: 4,-6
  output: -24
  expected: The sides of the rectangle cannot be negative
  ~~~
- perimeter()
###### Correct tests
- area()
- ~~~
  input: 4,6
  output: 20
  ~~~
  ~~~
  input: 4.4,6.6
  output: 22.0
  ~~~
  ~~~
  input: 4,0
  output: 8
  ~~~
  ###### Incorrect tests
- ~~~
  input: 4,-6
  output: -4
  expected: The sides of the rectangle cannot be negative
#### Square.py
###### Correct tests
- area()
- ~~~
  input: 3
  output: 9
  ~~~
  ~~~
  input: 3.5
  output: 12,5
  ~~~
  ~~~
  input: 0
  output: 0
  ~~~
  ###### Incorrect tests
- ~~~
  input: -3
  output: 9
  expected: The side of the square cannot be negative
  ~~~
- perimeter()
###### Correct tests
- area()
- ~~~
  input: 3
  output: 12
  ~~~
  ~~~
  input: 3.5
  output: 14
  ~~~
  ~~~
  input: 0
  output: 0
  ~~~
  ###### Incorrect tests
- ~~~
  input: -3
  output: -12
  expected: The side of the square cannot be negative
#### Triangle.py
###### Correct tests
- area()
- ~~~
  input: 5,7
  output: 17.5
  ~~~
  ~~~
  input: 5.5,7.7
  output: 21.175
  ~~~
  ~~~
  input: 5,0
  output: 0
  ~~~
  ###### Incorrect tests
- ~~~
  input: 5,-7
  output: -17,5
  expected: The base and height cannot be negative
  ~~~
- perimeter()
###### Correct tests
- area()
- ~~~
  input: 5,6,7
  output: 18
  ~~~
  ~~~
  input: 5.5,6.6,7
  output: 19.1
  ~~~
  ~~~
  input: 5,0,5.5
  output: 10.5
  ~~~
  ###### Incorrect tests
- ~~~
  input: 5,-6,7
  output: 6
  expected: The base and height cannot be negative
#### Circle
###### Correct tests
- area()
- ~~~
  input: 5
  output: 78.53981633974483
  ~~~
  ~~~
  input: 6.5
  output: 132.73228961416876
  ~~~
  ~~~
  input: 0
  output: 0
  ~~~
  ###### Incorrect tests
- ~~~
  input: -5b
  expected: The radius cannot be negative
  ~~~
- perimeter()
###### Correct tests
- area()
- ~~~
  input: 5
  output: 31.41592653589793
  ~~~
  ~~~
  input: 6.5
  output: 40.840704496667314
  ~~~
  ~~~
  input: 0
  output: 0
  ~~~
  ###### Incorrect tests
- ~~~
  input: -5
  expected: The radius cannot be negative

## Autotests succes:
~~~
- 32 - all tests;
- 8 - tests with errors;
- 24 - tests without errors;
~~~
- P with errors = 8/32 = 0,25
- P without errors = 24/32 = 0,75
~~~
- Tests with errors = 25%
- Tests without errors = 75%
~~~

# Commits
| Автор | Дата |  Хэш | Комментарий |
|---|---|---| --- |
| alinakhamatkhanova | Wed Nov 15 22:41:27 2023 +0300 | 08dfe6720f6ec2df9c05ba08266382e968b2620e | added four test |
| alinakhamatkhanova | Wed Nov 15 22:41:27 2023 +0300 | e00116108433034808ed6346fd26b74e6324dee9 | документация тесты к 4 файлам |