> !!! апдейт 15.11.23: добавлены юнит тесты для rectangle, circle, square, triangle !!!

<img width="200" height="150" alt="update apology" src="update-apology.gif"/>


# Общее описание проекта и функций (с примерами)
## circle.py
- содержит функцию area(r): принимает число r (радиус) и возвращает площадь круга по формуле S = πr^2
- содержит функцию perimeter(r): принимает число r (радиус) и возвращает периметр круга по формуле C = 2πr

### Примеры работы функций
**ввод**:
```python
print(area(2))
```
**вывод**:
```python
12.566370614359172 
```
---
**ввод**:
```python
print(perimeter(3))
```
**вывод**:
```python
18.84955592153876
```


## rectangle.py
- содержит функцию area(a, b): принимает числа a, b (стороны прямоугольника) и возвращает площадь прямоугольнкиа по формуле S = ab
- содержит функцию perimeter(a, b): принимает числа a, b (стороны прямоугольника) и возвращает периметр прямоугольнкиа по формуле P = 2(a+b)

### Примеры работы функций
**ввод**:
```python
print(area(10, 5))
```
**вывод**:
```python
50 
```
---
**ввод**:
```python
print(perimeter(10, 5))
```
**вывод**:
```python
30
```

## square.py
- содержит функцию area(a): принимает число a (сторона квадрата) и возвращает площадь квадрата по формуле S = a^2
- содержит функцию perimeter(a): принимает число a (сторона квадрата) и возвращает периметр квадрата по формуле P = 4a

### Примеры работы функций
**ввод**:
```python
print(area(6))
```
**вывод**:
```python
36
```
---
**ввод**:
```python
print(perimeter(5))
```
**вывод**:
```python
20
```

## triangle.py
- содержит функцию area(a, h): принимает числа a, h (a - катет, h - высота) и возвращает площадь прямоугольнкиа по формуле S = (1/2)ah
- содержит функцию perimeter(a, b, c): принимает числа a, b, c (стороны треугольника) и возвращает периметр треугольника по формуле P = a + b + c

### Примеры работы функций
**ввод**:
```python
print(area(10, 4))
```
**вывод**:
```python
20
```
---
**ввод**:
```python
print(perimeter(3, 4, 5))
```
**вывод**:
```python
12
```


# История изменений проекта
commit e6d663e3413f97114f08890d7523ddc592abe3b0 (HEAD -> main, origin/main, origin/HEAD)
Author: Sergei Khachatrian <51859273+sergothot@users.noreply.github.com>
Date:   Wed Oct 4 13:44:12 2023 +0300

    added commentary triangle.py

commit db79bba66fb739aa0010fa2f90395568227b60d5
Author: Sergei Khachatrian <51859273+sergothot@users.noreply.github.com>
Date:   Wed Oct 4 13:39:02 2023 +0300

    added commentary square.py

commit 9a7d7481666435796f124aa4de2332dfd09031c8
Author: Sergei Khachatrian <51859273+sergothot@users.noreply.github.com>
Date:   Wed Oct 4 13:37:36 2023 +0300

    added commentary rectangle.py

commit 3db00f849366bee5f7cec0e4a95342cc2681cdb3
Author: Sergei Khachatrian <51859273+sergothot@users.noreply.github.com>
Date:   Wed Oct 4 13:33:25 2023 +0300

    added commentary circle.py

commit 4ff4f2f2fbb1b2f4fdcf05ae2a9c9bc2366b7de7
Author: Sergei Khachatrian <51859273+sergothot@users.noreply.github.com>
Date:   Mon Sep 11 11:36:17 2023 +0300

    fixed perimeter formula error rectangle.py

commit df4857ab88165cad7c6b6117df44a59a026b6a2b
Author: Sergei Khachatrian <51859273+sergothot@users.noreply.github.com>
Date:   Mon Sep 11 10:32:27 2023 +0300

    added triangle.py

commit 057613269daa2d1165a259b88687aa84e29e3301
Author: Sergei Khachatrian <51859273+sergothot@users.noreply.github.com>
Date:   Mon Sep 11 10:03:56 2023 +0300

    added rectangle.py

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square added
