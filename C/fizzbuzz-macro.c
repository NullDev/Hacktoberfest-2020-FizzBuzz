// This program uses an macro which acts an function here, to print the values of FizzBuzz
// Author: @NadimintyKaundinya
#include <stdio.h>
#include <stdlib.h>
#define FIZZBUZZ(val) ((val % 15 == 0) ? sprintf(result, "%s", "FizzBuzz") : (val % 5 == 0 ? sprintf(result, "%s", "Buzz") : (val % 3 == 0 ? sprintf(result, "%s", "Fizz") : sprintf(result, "%d", val))))
char result[15];
int main()
{
    int n, i = 0;
    printf("Enter the value of n:");
    scanf("%d", &n);
    while (i++ < n)
    {
        FIZZBUZZ(i);
        printf("%s\n", result);
    }
    return 0;
}