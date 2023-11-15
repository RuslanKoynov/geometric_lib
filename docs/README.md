# Общее описание решения
1) В репзитории создал ветку documentation_409511
2) Создал файлы (rectangle_with_comments.py и triangle_with_comments.py) и написал комментарии в них, которые описывают работу функций
3) Добавил файл rectangle_with_comments.py и создал коммит с сообщением о том, что был добавлен новый файл
4) Добавил файл triangle_with_comments.py и создал коммит с сообщением о том, что был добавлен новый файл 
## Математические формулы
- ### Площадь
- Окружность: S = πR²
- Прямоугольник: S = ab
- Квадрат: S = a²
- Треугольник: S = a * h / 2
- ### Периметр
- Окружность: P = 2πR
- Прямоугольник: P = 2a + 2b
- Квадрат: P = 4a
- Треугольник: P = a * h / 2
- # Описание каждой функции с примерами вызова
- ## Circle:
- ### Площадь окружности
```
import math
def area(r):
    return math.pi * r * r
```
- **Пример работы**
<br>_input: 7_</br>
*output: 153.93804002589985*
- ### Периметр окружности
```
def perimeter(r):
    return 2 * math.pi * r
```
- **Пример работы**
<br>_input: 7_</br>
_output: 43.982297150257104_
- ## Rectangle:
- ### Площадь прямоугольника
```
def area(a, b): 
    return a * b 
```
- **Пример работы**
<br>_input: 6 7_</br>
*output: 42*
- ### Периметр прямоугольника
```
def perimeter(a, b): 
    return (a + b) * 2
```
- **Пример работы**
<br>_input: 7 6_</br>
_output: 26_
- ## Square:
- ### Площадь квадрата
```
def area(a): 
    return a * a
```
- **Пример работы**
<br>_input: 5_</br>
*output: 25*
- ### Периметр квадрата
```
def perimeter(a): 
    return a*4 
```
- **Пример работы**
<br>_input: 10_</br>
_output: 40_

- ## Triangle:
- ### Площадь треугольника
```
def area(a, h): 
    return a * h / 2
```
- **Пример работы**
<br>_input: 7 8_</br>
*output: 28*
- ### Периметр треугольника
```
def perimeter(a, b, c): 
    return a + b + c 
```
- **Пример работы**
<br>_input: 8 8 8_</br>
_output: 24_
- # История изменения проекта с хешами комитов (кроме последней записи)
- 3830d45eb9221b47023c07792c4d3ea0368545f0 Added file rectangle_with_comments.py
- f10d9bca3cf8a5b002a3f0f63c8dbf47a00dd9f6 File rectangle.py has been corrected
- fe2b3736a90cd0a0fbd7421dfd6e8fd0246fdcab Added new file
- d078c8d9ee6155f3cb0e577d28d337b791de28e2 L-03: Docs added
- 8ba9aeb3cea847b63a91ac378a2a6db758682460 L-03: Circle and square added
  - # Добавлены тесты для модулей
- ## Test log
- commit 35fad71bb7916c5f7bcd63368cb2b8d3c91fe6e3 (HEAD -> tests_409511, origin/tests_409511)
- Author: Coubick <samandr0405@gmail.com>
- Date:   Wed Nov 15 23:56:11 2023 +0300

  ```test: Added test for Circle```

- commit ca7cf912f757445a2f4f8c81b9488a598b55c2ea
- Author: Coubick <samandr0405@gmail.com>
- Date:   Wed Nov 15 23:54:00 2023 +0300

  ```test: Added test for Triangle```

- commit 977a54c8d29d0ca33914fc88b151526db54b93a3
- Author: Coubick <samandr0405@gmail.com>
- Date:   Wed Nov 15 23:49:27 2023 +0300

  ```test: Added test for Square```

- commit b6b9d41c5a19d63d8804397f9215569a0c4af5cd
- Author: Coubick <samandr0405@gmail.com>
- Date:   Wed Nov 15 23:12:31 2023 +0300

  ```test: Added test for Rectangle```
