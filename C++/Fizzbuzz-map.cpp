// FizzBuzz cpp solution using map 
// Author: @shashank-100
#include <iostream>
#include <unordered_map>
using namespace std;

int main()
{
    unordered_map<int,string> u;
    u[15]="FizzBuzz";
    u[5]="Buzz";
    u[3]="Fizz";
    for(int i=1;i<=100;i++){
      if(i%15==0)cout<<u[15];
      else if(i%5==0)cout<<u[5];
      else if(i%3==0)cout<<u[3];
      else cout<<i;
    }
}
