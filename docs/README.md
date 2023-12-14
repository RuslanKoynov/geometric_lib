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

# Общие описание решения 
В папке задержится 4 файла с функцими для нахождения площади и переметра для 4 фигур(круга, прямоугольника, триугольника и квадрата). Функции считывает параметры фигуры и выдаёт значения периметра и площади.


# Описание каждой функции с примером вызова

## Circle
```nginx
[Python]
import math
def area(r):
    '''Принимает число r, возвращает площадь круга с радиусом равным r'''
    return math.pi * r * r


def perimeter(r):
    '''Принимает число r, возвращает периметр круга с радиусом равным r '''
    return 2 * math.pi * r
```
### Примеры входных данных
```nginx
print(area(2))
print(perimeter(3))
```

### Примеры выходных данных
```nginx
12.566370614359172 
18.84955592153876
```

## Rectangle
```nginx
[Python]
import math
def area(a, b): 
    '''Принимает числа a и b, возвращает площадь прямоугольника со сторонами a и b'''
    return a * b 

def perimeter(a, b):
    '''Принимает числа a и b, возвращает периметр прямоугольника со сторонами a и b''' 
    return 2*(a + b)

```
### Примеры входных данных 
```nginx
print(area(2, 3))
print(perimeter(2, 3))
```

### Примеры выходных данных
```nginx
6
10
```

## Square
```nginx
[Python]
import math
def area(a):
    '''Принимает число a, возвращает площадь квадрата со стороной a'''
    return a * a


def perimeter(a):
    '''Принимает число a, возвращает периметр квадрата со стороной a'''
    return 4 * a

```
### Примеры входных данных 
```nginx
print(area(2))
print(perimeter(3))
```
### Примеры выходных данных
```nginx
4
12
```

## Triangle

```nginx
[Python]
import math
def area(a, h):
    ''''Принимает числа a и h, возвращает площадь треугольника cо стороной a и высотой h'''
    return a * h / 2 

def perimeter(a, b, c):
    ''''Принимает числа a, b и c, возвращает периметр треугольника cо стороной a,b и c'''
    return a + b + c
```
### Примеры входных данных
```nginx
print(area(2, 3))
print(perimeter(1, 2, 3))
```

### Примеры выходных данных
```nginx
3
6
```
# Ручные тесты
X=27 (всего было создано 27 тестов)

Y=17 (успешно пройденно 17)

P=63% (процент успешного выполнения теста)
# История изменения проекта с хешами комитов
| Hash | Author  | Date  |
|--------|-------|-------|
| c43bf12|  Mogohars <Qweqweqwe1232005@gmail.com>| Wed Dec 13 16:19:42 2023|
| 6ebca62 |  Mogohars <Qweqweqwe1232005@gmail.com>|Wed Oct 4 19:48:20 2023|
| a0967ca |  Mogohars <Qweqweqwe1232005@gmail.com>|Wed Sep 20 20:13:05 2023|
| a2e7358 | Mogohars <Qweqweqwe1232005@gmail.com>|  Wed Sep 20 20:10:36 2023|
| d078c8d | smartiqa <info@smartiqa.ru>|  Thu Mar 4 14:55:29 2021 |
| 8ba9aeb | smartiqa <info@smartiqa.ru> |  Thu Mar 4 14:54:08 2021 |