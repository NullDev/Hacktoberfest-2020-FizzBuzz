// Not the most concise or memory efficient Fizz Buzz variant, but is easy to add more conditions such as (i % 4 == 0)
// FizzBuzz usually only prints out the first 100 numbers, but if you want more or less you have the option to.
// This program has a runtime of O(n) or linear because the time to run increases with the number of iterations linearly
// Author: @StephenTrainor

#include <stdio.h>

int main(void) {
    int iterations;
    printf("Enter number to go up to: ");
    scanf("%d", &iterations);
    for (int i = 1; i < iterations; i++) {
        if (i % 3 == 0) {
            printf("Fizz");
        }
        if (i % 5 == 0) {
            printf("Buzz");
        }
        if ((i % 5 != 0) && (i % 3 != 0)) {
            printf("%i", i);
        }
        printf("\n");
    }
}
