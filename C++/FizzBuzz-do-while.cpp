//A C++ code to get FizzBuzz from 1 to 100
//Author: @AyushVarma

#include<bits/stdc++.h>
using namespace std;

int main(){
    int i=0;
    do{
        i++;
        if(i%3==0 && i%5==0) cout<<"FizzBuzz"<<endl;
        else if(i%5==0) cout<<"Buzz"<<endl;
        else if(i%3==0) cout<<"Fizz"<<endl;

    }while(i<=100);
    return 0;
}