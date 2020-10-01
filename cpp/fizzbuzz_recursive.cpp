// Recursive Fizzbuzz in C++
// Author: yadav-aman

#include<iostream>

int fizz(int n){
    if (n==101)
        return 0;
    if (n%3 == 0 && n%5 == 0)
        std::cout<<"FizzBuzz ";
    else if (n%5 == 0)
       std::cout<<"Buzz ";
    else if (n%3 == 0)
       std::cout<<"Fizz ";
    else
        std::cout<<n<<" ";
    return fizz(n+1);
}

int main(){
    fizz(1);
    return 0;
}
