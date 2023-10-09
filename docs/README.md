# **Документация**
### *В данном репозитории находятся файлы с функциями для вычислению площади и периметра разных геометрических фигур*
## Math formulas
### Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ah/2

### Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

# Файлы:

## Circle.py
- ### Функция area - вычисляет площадь из полученного от пользователя радиуса(r) при помощи формулы 'πR²'
#### Пример работы:
```python
[Python]
import circle

circle area(2) = 12,5
```

- ### Функция perimeter - вычисляет периметр из полученного от пользователя радиуса(r) при помощи формулы '2πR'
#### Пример работы:
```python
[Python]
import circle

circle perimeter(9) = 56,5
```

## Rectangle.py
- ### Функция area - вычисляет площадь из полученных от пользователя значений a и b при помощи формулы 'ab'
#### Пример работы:
```python
[Python]
import rectangle

rectangle area(2, 2) = 4
```

- ### Функция perimeter - вычисляет периметр из полученных от пользователя значений a и b при помощи формулы '2a + 2b'
#### Пример работы:
```python
[Python]
import rectangle

rectangle perimeter(2, 2) = 8
```

## Square.py
- ### Функция area - вычисляет площадь из полученного от пользователя значения a при помощи формулы 'a²'
#### Пример работы:
```python
[Python]
import square

rectangle area(3) = 9
```

- ### Функция perimeter - вычисляет периметр из полученного от пользователя значения a при помощи формулы '4a'
#### Пример работы:
```python
[Python]
import square

rectangle perimeter(3) = 12
```

## Triangle.py
- ### Функция area - вычисляет площадь из полученных от пользователя значений a - стороны треугольника и h - высоты треугольника при помощи формулы '(a * h)/2'
#### Пример работы:
```python
[Python]
import triangle

rectangle area(3, 4) = 6
```

- ### Функция perimeter - вычисляет периметр из полученных от пользователя значений a, b, c - сторон треугольника при помощи формулы 'a + b + c'
#### Пример работы:
```python
[Python]
import triangle

rectangle perimeter(3, 4, 5) = 12
```

| Хэш коммита | Автор     | Комментарий                        |
|-------------|-----------|------------------------------------|
| 7455f2d     | RomoBomba | Added a comment to the triangle.py |
| 343bc38     | RomoBomba | Added a comment to the square.py   |
| e5f92d9     | RomoBomba | Added a comment to the rectangle   |
| 528b3c1     | RomoBomba | Added a comment to the code        |
| d85e206     | RomoBomba | Fixed file                         |
| 4af1c65     | RomoBomba | Added new file                     |
| d078c8d     | smartiqa  | Docs added                         |
| 8ba9aeb     | smartiqa  | Circle and square added            |