#include <iostream>
using namespace std;
int main()
{
    int n=1;
    top:
    if(n>100) return 0;
    if(!(n%3) && !(n%5)) cout<<"fizzbuzz\n";
    else if(!(n%3)) cout<<"fizz\n";
    else if(!(n%5)) cout<<"buzz\n";
    n++;
    goto top;
}
