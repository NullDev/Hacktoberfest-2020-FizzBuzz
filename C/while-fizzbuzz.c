// Using while loop and ? : (Ternary operator)
// Author @NidhxGupta

#include <stdio.h>

int main(void)
{
    int i = 1;

    while(i < 101)
    {
        (i % 3 == 0 && i % 5== 0) ? printf("FizzBuzz\n") : (i % 3 == 0) ? printf("Fizz\n") :( (i % 5 == 0) ? printf("Buzz\n") : printf("%d\n",i) );

        i++; //Incrementing i by 1
    }

    return 0;
}