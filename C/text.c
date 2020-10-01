#include<stdio.h>
void main()
{
    for (i = 1; i<= 100; i++)
    {
        x = (i % 3 == 0 && i % 5 == 0) ? "FizzBuzz" : ( i%3 == 0 ? : "Fizz" : ( i%5 == 0 ? "Buzz" : i) );
        printf("x\n");
    }
}