# Math formulas

##Общее описание решения


## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

##Описание каждой функции с примерами вызова

- square functions

Площадь

```python
 def area(a):
    return a * a
    '''Принимает значение a,возвращает a в квадрате'''
```

**Пример вызова**

```python
print(area(16))
```

**Пример вывода**

```python
256
```
Периметр

```python
def perimeter(a):
    '''Принимает значение a,возвращает произведение 4 на a'''
    return 4 * a
```

**Пример вызова**

```python
print(perimeter(5))
```

**Пример вывода**

```python
20
```

- circle functions

Площадь

```python
def area(r):
    '''Принимает число r,возвращает произведение math.pi и r в квадрате'''

    return math.pi * r * r
```

**Пример вызова**

```python
print(area(3))
```

**Пример вывода**

```python
28.274333882308138
```

Периметр

```python 
def perimeter(r):
    '''Принимает число r,возвращает произведение удвоенного math.pi и r'''
    return 2 * math.pi * r
```

**Пример вызова**

```python
print(perimeter(3))
```

**Пример вывода**

```python
18.84955592153876
```

- rectangle functions

Площадь

```python
def area(a, b):
    '''Принимает число a и b,возвращает произведение a и b'''
    return a * b
```

**Пример вызова**

```python
print(area(3,5))
```

**Пример вывода**

```python
15
```

Периметр

```python
def perimeter(a, b):
    '''Принимает число a и b,возвращает удвоенную сумму a и b'''
    return (a + b) * 2
```

**Пример вызова**

```python
print(area(3,7))
```

**Пример вывода**

```python
20
```

- triangle functions

Площадь

```python
def area(a, h):
    '''Принимает число a и h,возвращает произведение a и h деленную на 2'''
    return a * h / 2
```

**Пример вызова**

```python
print(area(5,2))
```

**Пример вывода**

```python
5
```

Периметр

```python
def perimeter(a, b, c):
    '''Принимает число a и b и c,возвращает сумму a,b,c'''
    return a + b + c
```

**Пример вызова**

```python
print(perimeter(5,6,7))
```

**Пример выовда**

```python
18
```


## Tests
- Успешные тесты: 16/18 (89%)


##История изменения проекта

| Hash | Date | Author | Comment |  
|:------------------------------|:-----------------------------:|------------------------------:|:--------------------------|
| 8ba9aeb3ce | Thu Mar 4 14:54:08 2021 | smartiqa <info@smartiqa.ru> | Circle and square added |
| d078c8d9ee | Thu Mar 4 14:55:29 2021 | smartiqa <info@smartiqa.ru> | Docs added |
| fe0e53a86 |  Mon Sep 18 17:23:17 2023 | Джабаров Саид <dsaidik123@gmail.com> | new file added |
| 16b4f40f7 |  Mon Sep 18 17:30:07 2023 | Джабаров Саид <dsaidik123@gmail.com> | bug fix |
| 59945b139 |  Wed Oct 4 22:15:05 2023 | Джабаров Саид <dsaidik123@gmail.com> | docs: aded comments to all functions|
| 0340c042e96d2e583fcd5c8349f4ab6e93bc9d6a | Thu Nov 16 02:55:01 2023 | Джабаров Саид dsaidik123@gmail.com |  added unittests |
| 250be8f77a67ce2e78b2b64a5918f08387f64b54 | Thu Nov 16 02:04:33 2023 | Джабаров Саид <dsaidik123@gmail.com> |  test: unittests |

