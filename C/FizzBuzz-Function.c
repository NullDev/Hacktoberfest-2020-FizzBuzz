/* FizzBuzz programming using a function in C language
Author: @TarunJana */
#include <stdio.h>

int main() {
    int i;
    for(i=1;i<=100;i++)
    FizzBuzz(i);
    return 0;
}
/* FizzBuzz Function*/
int FizzBuzz(int i)
{
    if (i%3==0 && i%5==0) printf("FizzBuzz\n");
    else if (i%3==0) printf("Fizz\n");
    else if (i%5==0) printf("Buzz\n");
    else printf("%d\n",i);
    return 0;
}
