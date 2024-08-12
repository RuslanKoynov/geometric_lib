# Лобораторная работа №2
## lol.cpp
```C++
#include <iostream>
using namespace std;
string bit(long long &x){
    string line="";
    while(x!=0){line=to_string(x%2)+line;x/=2;}
    return line;
}
int main() {
    long long X,Y;
    cin>>X>>Y;
    std::cout<<bit(X)<<" "<<bit(Y);
    return 0;
}

```


#### string bit
>  ##### Возращает двоичную форму числа
>  ##### Параметры ввода:
>>    long long x - число в десятичной форме 
>  ##### Параметры вывода:
>>    String line - число в двоичной форме
***


## square.py
```python
def area(a):
    return a * a


def perimeter(a):
    return 4 * a

```


#### def area(a)
>  ##### Возращает площадь квадрата
>  ##### Параметры ввода:
>>    int a - сторона квадрата
>  ##### Параметры вывода:
>>    int a**2 - площадь квадрата
#### def perimeter(a)
>  ##### Возращает периметр квадрата
>  ##### Параметры ввода:
>>    int a - сторона квадрата
>  ##### Параметры вывода:
>>    int a*4 - периметр квадрата
***


## triangle.py
```python
def area(a, h): 
    return a * h / 2 

def perimeter(a, b, c): 
    return a + b + c 

```
#### def area(a, h)
>  ##### Возращает площадь треугольника
>  ##### Параметры ввода:
>>    int a - сторона треугольника
>>    int h - высота проведённая к этой стороне
>  ##### Параметры вывода:
>>    int a * h / 2 - площадь треугольника
 #### perimeter(a, b, c)
>  ##### Возращает периметр треугольника
>  ##### Параметры ввода:
>>    int a - сторона треугольника
>>    int b - сторонп треугольника
>>    int c - сторона треугольника
>  ##### Параметры вывода:
>>    int a + b + c - периметр треугольника
***
# История изменений
 1. в ветку new_features409031 добавлен новый файл rectangle.py
  комит " New fayl " ***8ba9aeb3cea847b63a91ac378a2a6db758682460***
 2. в ветку new_features409031 добавлен новый файл triangle.py исправлена ошибка в файле rectangle.py 
 3. комит "New file" ***d078c8d9ee6155f3cb0e577d28d337b791de28e2***
 4. создана ветка  ***8cee8afc5947d43da3fc39e2d0a2b46a0356f7dd***
 5. добывлен файл lol.cpp ***11b87f0614fde5b79e18d24e5b36bb878d026bf3***
