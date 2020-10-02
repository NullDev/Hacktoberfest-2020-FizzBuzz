// FizzBuzz with boolean logic 
// Author: @ankitsridhar16

#include<iostream>

inline void isFizzBuzz(bool& fizz , bool& buzz, uint_fast16_t& maxNum)
{
    if(fizz && buzz)
        std::cout << "FizzBuzz" << "\n";
    else if(fizz && !buzz)
        std::cout << "Fizz" << "\n";
    else if(buzz && !fizz)
        std::cout << "Buzz" << "\n";
    else if(!buzz && !fizz) 
        std::cout << std::to_string(maxNum) << "\n";
}


int main()
{
    uint_fast16_t maxNum = 1, limit = 0; 
    std::cin >> limit; 
    bool fizz = false , buzz = false;
    while(maxNum <= limit)
    {
        fizz = maxNum%3==0;
        buzz = maxNum%5==0;
        isFizzBuzz(fizz,buzz,maxNum);
        ++maxNum;
    }
    return 0;
}