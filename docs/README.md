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
    ''' функция на вход принимает значение а и возвращает квадрат числа а'''

Пример вызова

   print(area(3))

   Пример вывода
   9
   Периметр

python
def perimeter(a):
    ''' функция на вход принимает значение а и возвращает 4 * a'''
    return 4 * a

Пример вызова

    python
    print(perimeter(2))

    Пример вывода

    python
    8

- circle functions

Площадь

    python
    def area(r):
        ''' функция принимает значение n, возвращает значение 3.14*r**2(площадь окружности)'''

        return math.pi * r * r

    Пример вызова

    python
    print(area(3))

    Пример вывода

    python
    28.274333882308138

Периметр

    python 
    def perimeter(r):
       '''Принимает число r,возвращает произведение удвоенного math.pi и r'''
    return 2 * math.pi * r

Пример вызова

    python
    print(perimeter(3))

    Пример вывода

    python
    18.84955592153876

- rectangle functions

    def area(a, b):
    '''принимает значение  a и b на вход,возвращает произведение a и b'''
    return a * b

    Примеры вызова

    print(area(7,9))
    Примеры вывода
    63

def perimeter(a, b): 
    ''' функция принимает значения а и b и возвращает сумму а и b, умноженную на 2(периметр прямоугольника)'''
    return (a + b) * 2

    Примеры вызова 
    print(perimetr(3,2))
    Примеры вывода
    12

    python
```
| Hash | Date | Author | Comment |  
|:------------------------------|:-----------------------------:|------------------------------:|:--------------------------|
| 8ba9aeb3ce | Thu Mar 4 14:54:08 2021 | smartiqa <info@smartiqa.ru> | Circle and square added |
| d078c8d9e | Thu Mar 4 14:55:29 2021 | smartiqa <info@smartiqa.ru> | Docs added |
| df9262113 |  Wed Sep 20 17:47:32 2023 |  capybara1991 <pprostakovich@gmail.com> |  File was added |
| bf53ba5cb |  Wed Sep 20 17:54:27 2023 | capybara1991 <pprostakovich@gmail.com> | Problem was fixed |
| 8b11bb564 | Wed Oct 4 23:08:35 2023 | capybara1991 <pprostakovich@gmail.com>|  docs: comments were added to all functions|