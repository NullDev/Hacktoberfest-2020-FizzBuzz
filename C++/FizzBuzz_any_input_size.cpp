//Program to implement the fizzbuzz solution

#include<iostream>
#include<bits/stdc++.h>

using namespace std;

int main()
{
    long long int num,i;
    cin>>num;
    for(i=1;i<num;i++)
    {
        if(i%3==0&&i%5==0)
        cout<<"FizzBuzz"<<endl;
        else if (i%5==0)
        cout<<"Buzz"<endl;
        else
        cout<<"Fizz"<<endl;
    }
}
