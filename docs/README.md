# circle.py
## def area(r):
- считает по радиусу площадь круга
- S = πR²
- пример area(3) = 28.274333882308138
## def perimeter(r):
- считает по радиусу периметр круга
- P = 2πR
- пример perimeter(3) = 18.84955592153876

# rectangle.py
## def area(a, b):
- считает площадь прямоугольника по 2 его сторонам 
-  S = ab
-  пример area(2, 13) = 26
## def perimeter(a, b):
- считает периметр прямоугольника по 2 его сторонам 
- P = 2a + 2b
- пример perimeter(2, 3) = 10

# square.py
## def area(a):
- считает площадь квадрата по его стороне 
- S = a²
- пример area(4) = 16
## def perimeter(a):
- считает периметр квадрата по его стороне 
- P = 4a
- пример perimeter(2) = 8

# triangle.py
## def area(a, h): 
- считает площадь треугольника по его стороне и опущенной к ней высоте
- S = a * h / 2
- пример area(2, 5) = 5
## def perimeter(a, b, c):
- считает периметр треугольника по его трем сторонам
- P = a + b + c
- пример perimeter(1, 2, 3) = 6

# История коммитов
- commit 8ba9aeb3cea847b63a91ac378a2a6db758682460 L-03: Circle and square added
- commit d078c8d9ee6155f3cb0e577d28d337b791de28e2 L-03: Docs added
- commit 23fffcb08df0ce4d2eadbd884aa531b4d85d32f9 added new file rectangle.py
- commit 81792a015ce88b26516d0d306b3a63d1fe9a6a66 added new file triangle.py; fixed 1 issue in rectangle.py
- commit e1a48474007586be4f80cfbb8d2b549c3c77bc68 documentation
- commit 66a87e0d2744b4008f51fa5f30a8bcf435bc57df documentation
- commit 9c8192bae3dda90eeacb7485a9e586310c2d350f documentation
- commit 9c8192bae3dda90eeacb7485a9e586310c2d350f documentation



# Unit тесты

## circleTests.py (для circle.py)

| Test name               | Input             | Expected output    | True / False | Description                 |
|-------------------------|-------------------|--------------------|--------------|-----------------------------|
| test_zero_area          | area( 0)          | 0                  | True         | -                           |
| test_one_area           | area( 1)          | 3.141592653589793  | True         | -                           |
| test_float_area         | area( 2.5)        | 19.634954084936208 | True         | -                           |
| test_negative_area      | area(- 5)         | 78.53981633974483  | True         | radius can't be negative    |
| test_string_area        | area( "123")      | 47529.15525615998  | False        | can't work with strings     |
| test_zero_perimeter     | perimeter( 0)     | 0                  | True         | -                           |
| test_one_perimeter      | perimeter( 1)     | 6.283185307179586  | True         | -                           |
| test_float_perimeter    | perimeter( 2.5)   | 15.707963267948966 | True         | -                           |
| test_negative_perimeter | perimeter(- 5)    | 31.41592653589793  | False        | perimeter can't be negative |
| test_string_perimeter   | perimeter( "123") | 772.8317927830891  | False        | can't work with strings     |



## rectangleTests.py (для rectangle.py)

| Test name               | Input                  | Expected output | True / False | Description                            |
|-------------------------|------------------------|-----------------|--------------|----------------------------------------|
| test_zero_area          | area( 0 ,  123)        | 0               | True         | -                                      |
| test_one_area           | area( 1 ,  123)        | 123             | True         | -                                      |
| test_float_area         | area( 2.5 ,  3)        | 7.5             | True         | -                                      |
| test_negative_area      | area(- 5 ,  2)         | 10              | False        | side can't be negative                 |
| test_string_area        | area( "123" ,  2)      | 246             | False        | can't work with string                 |
| test_zero_perimeter     | perimeter( 0 ,  123)   | 0               | False        | if side is 0 the perimeter should be 0 |
| test_one_perimeter      | perimeter( 1 ,  123)   | 248             | True         | -                                      |
| test_float_perimeter    | perimeter( 2.5 ,  3)   | 11.0            | True         | -                                      |
| test_negative_perimeter | perimeter(- 5 ,  2)    | 6               | False        | side can't be negative                 |
| test_string_perimeter   | perimeter( "123" ,  2) | 250             | False        | can't work with string                 |



## squareTests.py (для square.py)

| Test name               | Input             | Expected output | True / False | Description             |
|-------------------------|-------------------|-----------------|--------------|-------------------------|
| test_zero_area          | area( 0)          | 0               | True         | -                       |
| test_one_area           | area( 1)          | 1               | True         | -                       |
| test_float_area         | area( 2.5)        | 6.25            | True         | -                       |
| test_negative_area      | area(- 5)         | 25              | False        | side can't be negative  |
| test_string_area        | area( "123")      | 15129           | False        | can't work with strings |
| test_zero_perimeter     | perimeter( 0)     | 0               | True         | -                       |
| test_one_perimeter      | perimeter( 1)     | 4               | True         | -                       |
| test_float_perimeter    | perimeter( 2.5)   | 10              | True         | -                       |
| test_negative_perimeter | perimeter(- 5)    | 20              | False        | side can't be negative  |
| test_string_perimeter   | perimeter( "123") | 492             | False        | can't work with strings |



## triangleTests.py (для triangle.py)

| Test name               | Input                           | Expected output | True / False | Description             |
|-------------------------|---------------------------------|-----------------|--------------|-------------------------|
| test_zero_area          | area( 0 ,  2)                   | 0               | True         | -                       |
| test_one_area           | area( 1 ,  2)                   | 1               | True         | -                       |
| test_float_area         | area( 2.5 ,  2)                 | 2.5             | True         | -                       |
| test_negative_area      | area(- 5 ,  10)                 | 25              | False        | side can't be negative  |
| test_string_area        | area( "123" ,  2)               | 123             | False        | cant't work with string |
| test_zero_perimeter     | perimeter( 0 ,  1 ,  2)         | 0               | True         | -                       |
| test_one_perimeter      | perimeter( 1 ,  2 ,  3)         | 6               | True         | -                       |
| test_float_perimeter    | perimeter( 2.5 ,  2.5 ,  2.5)   | 7.5             | True         | -                       |
| test_negative_perimeter | perimeter(- 5 ,  - 1 ,  - 4)    | 10              | False        | sides can't be negative |
| test_string_perimeter   | perimeter( "123" ,  "1" ,  "2") | 126             | False        | can't work with strings |



# Информация о тестах
- Тесты не охватывают всех возможных значений, которые могут принимать функции. В таблицах к каждому файлу представлена информация о тестах, верном или неверном их прохождении, при надобности написано описание тесту (как правило там находится предположение, почему возникла ошибка).
