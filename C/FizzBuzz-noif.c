// A script/program that solves FizzBuzz without using an if, if else, or else statement
// This program has a runtime of O(n) or linear (i think)
// Author: @StephenTrainor

#include <stdio.h>

int main(void) {
    double iterations;
    int fizz_case;
    int buzz_case;
    int random_variable;
    printf("Enter number to go up to: ");
    scanf("%lf", &iterations);
    for (int i = 1; i < iterations; i++) {
        random_variable = 0;
        fizz_case = i % 3;
        buzz_case = i % 5;
        switch(fizz_case) {
            case 0: {
                printf("Fizz");
                random_variable++;
                break;
            }
        }
        switch(buzz_case) {
            case 0: {
                printf("Buzz");
                random_variable++;
                break;
            }
        }
        switch(random_variable) {
            case 0: {
                printf("%i", i);
            }
        }
        printf("\n");
    }
}
