#include <iostream>
using namespace std;
string bit(long long &x){
    /*
    Возращает двоичную форму числа
       
       Параметры:
                x(long long) : десятичное число
        
       Возрощаемое значение:
                line(string) : строка содержащия в себе двоичную форму числа

    */
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
