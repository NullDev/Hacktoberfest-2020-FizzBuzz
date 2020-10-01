; FizzBuzz code in C
; Author: @nchiarappa

#include <stdio.h>
#include <stdlib.h>

int main()
{
   int i = 1;
   for (; i<=100; ++i) {
      printf("number is %d %s%s\n", i, i%3?"":"Fizz", i%5?"":"Buzz");
   }
   return 0;
}