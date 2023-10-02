#include <iostream>
using namespace std;
string bit(long long &x){
    string line="";
    while(x!=0){line=to_string(x%2)+line;x/=2;}
    return line;
}
void perevod(string &line){
    int starter=line.find('1',line.find('0'));
    if(starter==-1)starter=line.size()-1;
    for(starter;starter<line.size();starter++)line[starter]='1';
}
int perevod_k_step(string &line){
    int count= line.find('1',line.find('0'))-line.find('0');
    int stoper=line.find('0');
    stoper++;
    while(stoper!=line.size()-1){count+=line.size()-1-stoper;stoper++;}
    return count;
}
int stepeni(long long x,long long y){
    int count=0;
    while(x!=y){count+=x*(x-1)/2;x++;}
    return count;
}
int main() {
    long long X,Y;
    cin>>X>>Y;
    string str_X,str_Y;
    str_X=bit(X);str_Y= bit(Y);
    string before=str_Y;
    perevod(str_X);perevod(str_Y);
    int count_x=perevod_k_step(str_X),count_y= perevod_k_step(str_Y);
    int count_step= stepeni(str_X.size(),str_Y.size());
    if(before==str_Y)cout<<count_step-count_y+count_x+1;
    else cout<<count_step-count_y+count_x;
    return 0;
}
