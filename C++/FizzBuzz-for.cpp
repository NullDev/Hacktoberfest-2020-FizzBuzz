//Multiples of 3,5,3&5
// Author : @cruiz24 

#include<iostream>
 using namespace std;

int main(){
 int i;
 char f;
  for(i=1;i<=100;i++){
        cout<<"\n\t";
  if((i%3==0)&&(i%5==0))
       cout<<"FizzBuzz";
    else if(i%3==0)
        cout<<"Fizz";
    else if(i%5==0)
        cout<<"Buzz";
    else
        cout<<i;
  }
return 0;
  }
