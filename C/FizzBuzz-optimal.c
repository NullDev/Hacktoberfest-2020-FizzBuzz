// A script/program that solves FizzBuzz
// This program has a runtime of O(n) or linear (i think)
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
