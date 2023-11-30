# Функции для вычисления площадей и периметров геометрических фигур
## Общее описание решения
Набор функций для вычисления площади и периметра квадрата, прямоугольника, окружности и треугольника. 

## Описание фунций


### circle.py  
 **Функция area(r)**  

Принимает значение радиуса окружности, возвращает значение площади круга 

Ввод:  
```
import circle
print(circle.area(5))  
```  
Вывод:  
```
78.53981693250938
```
**Функция perimeter(r)**  

Принимает значение радиуса окружности, возвращает значение длины окружности 

Ввод:  
```
import circle
print(circle.perimeter(5))  
```  
Вывод:  
```
31.41592653589793 
```
    
### rectangle.py
**Функция area(a, b)**  

Принимает значения длин сторон прямоугольника, возвращает значение площади  

Ввод:  
```
import rectangle
print(rectangle.area(4, 5))  
```  
Вывод:  
```
20 
```
**Функция perimeter(a, b)**  

Принимает значения длин сторон прямоугольника, возвращает значение периметра  

Пример вызова:  
```
import rectangle
print(rectangle.perimeter(4, 5))  
```  
Вывод:  
```
18  
```
### square.py  
**Функция area(a)**  

Принимает знчение длины стороны квадрата, возвращает значение периметра квадрата  

Ввод:  
```
import square
print(square.area(5))  
```  
Вывод:  
```
25  
```
**Функция perimeter(a)**  

Принимает значение длины стороны квадрата, возвращает значение площади квадрата  

Ввод  
```
import square
print(square.perimeter(5))  
```  
Вывод:  
```
20  
```
### triangle.py  
**Функция area(a, h)**  

Принимает значение длин основания и высоты треугольника, возвращает значение площади треугольника

Ввод:  
```
import triangle
print(triangle.area(5, 5))  
```  
Вывод:  
```
12.5  
```
**Функция perimeter(a, b, c)**  
Принимает значения длин сторон треугольника, возвращает значение периметра треугольника 

Ввод:  
```
import triangle
print(triangle.perimeter(5, 5, 5))  
```  
Вывод:   
```
15  
```
## Тесты
Проведены ручные тесты описанных функций. Проведены Unit-тесты описанных функций
## История изменения проекта

commit 79e868c55018628ab4f41fe78b01ba5eac0019f6 (HEAD -> documentation_409094)
Author: nxrmxlnx <mdima0819@gmail.com>
Date:   Tue Oct 3 21:01:26 2023 +0700

    docs: declared functions in files

commit 20477b25151b832d32570b5c431ae8545ddaa08e (origin/main, origin/HEAD, main)
Author: nxrmxlnx <mdima0819@gmail.com>
Date:   Tue Sep 12 03:30:09 2023 +0700

    исправлена ошибка

commit 6e844695b110ede153628e899e5ca5a7f59a5498
Author: nxrmxlnx <mdima0819@gmail.com>
Date:   Tue Sep 12 03:26:29 2023 +0700

    добавлен новый файл

commit d078c8d9ee6155f3cb0e577d28d337b791de28e2
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:55:29 2021 +0300

    L-03: Docs added

commit 8ba9aeb3cea847b63a91ac378a2a6db758682460
Author: smartiqa <info@smartiqa.ru>
Date:   Thu Mar 4 14:54:08 2021 +0300

    L-03: Circle and square added

commit 41e6874d1ce73e5d34b7c17196cd125c9d74e005 (HEAD -> test_409094, origin/test_409094)
Author: nxrmxlnx <mdima0819@gmail.com>
Date:   Tue Nov 28 18:24:45 2023 +0700

    test: add new tests

