//fizzbuzz algorithm for different multiples of 3,5,15.
//Auther: @nausherofficial
#include <iostream>

using namespace std;

int main()
{
    char choice;

    do
    {
    int value;
    cout<<"enter any integer";
    cin>>value;
    if (value>1)
    {
        if(value%15==0)
            cout<<"fizzbuzz";
        else if(value%5==0)
            cout<<"buzz";
        else if(value%3==0)
            cout<<"fizz";
        else
            cout<<"try another number";
    }

    cout<<"\nenter 'Y' to check more values";
    cin>>choice;
    }
    while(choice=='y'|| choice=='Y');



}
