# Документация
В проекте содержатся математические формулы для нахождения площади и периметра геометрических фигур
## Rectangle

### Функция area 
Получает значение переменных `a` и `b`, после чего возвращает площадь прямоугольника (a*b).

#### Пример работы:
```python
[Python]
import rectangle

rectangle.area(4, 2) = 8
```


### Функция perimeter 
Получает значение переменных  `a` и `b`, после чего возвращает периметр прямоугольника 2*(a+b).

#### Пример работы:
```python
[Python]
import rectangle

rectangle.perimeter(2, 5) = 14
```

## Circle

### Функция area 
Получает значение переменной `r` - радиус, после чего возваращает площадь круга (pi на r квадрат)

##### Примеры работы:
```python
[Python]
import circle

circle.area(10) = 314
```

### Функция perimetr
Получает значение переменной `r`, что явялется радиусом, возвращает периметр круга (произведение 2 * pi * r)

##### Примеры работы:
```python
[Python]
import circle

circle.perimetr(10) = 62.8
```

## Triangle

### Функция area
Получает значение переменных `a`, `h`,после чего  возвращает периметр треугольника (a * h / 2)

##### Примеры работы:
```python
[Python]
import triangle

triangle.area(9, 4) = 18
```

### Функция perimetr
Получает значение переменных `a`, `b`, `c`, после чего  возвращает периметер треугольника (а + b + c)

##### Примеры работы:
```python
[Python]
import triangle

triangle.perimetr(1, 7, 3) = 11
```

## Square

### Функция area
Получает значение переменной `a`,после чего  возвращает площадь квадрата (a*a)

##### Примеры работы:
```python
[Python]
import square

square.area(20) = 400
```

### Функция perimetr
Получает значение переменной `a`, после чего  возвращает периметер квадрата (4 * a)

##### Примеры работы с функцией
```python
[Python]
import square

square.perimetr(8) = 32
```


| Хэш коммита  | Автор коммита  | Описание                |
|--------------|----------------|-------------------------|
| 0cd16c3      | NaumJan        | add triangle            |
| e16f8e5      | NaumJan        | add square              |
| d998222      | NaumJan        | add rectangle           |
| a2f4c64      | NaumJan        | add circle              |
| ab6f910      | NaumJan        | error fix               |
| d4bc4f5      | NaumJan        | add rectangle           |
| d078c8d      | smartiqa       | Docs added              |
| 8ba9aeb      | smartiqa       | Circle and square added |
