// I've solved this problem using C language. To check the results, type ./fizzbuzz in the terminal.
// Author: @NidhxGupta

/* FizzBuzz is a program that prints the numbers from 1 to 100. But for multiples of three it prints “Fizz” 
instead of the number and for the multiples of five, it prints “Buzz”. For numbers which are multiples of both three 
and five it prints “FizzBuzz”. */

#include <stdio.h>

int main()
{
    for (int i=1; i<=100; i++)
    {
        (i % 3 == 0 && i % 5== 0) ? printf("FizzBuzz\n") : (i % 3 == 0) ? printf("Fizz\n") :( (i % 5 == 0) ? printf("Buzz\n") : printf("%d\n",i) );
    }

    return 0;
}