//FizzBuzz in C
//Author: Siddhant Mittal(siddhantmittal024)

#include <stdio.h>
int main(void)
{
    int i;
    for (i=1; i <= 100; ++i)
    {
        printf("Number: %d %s%s\n", i, i % 3 ? "" : "Fizz", i % 5 ? "" : "Buzz");
    }
    return 0;
}
