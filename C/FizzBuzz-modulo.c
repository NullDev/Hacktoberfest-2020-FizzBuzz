// Completes the FizzBuzz challenge without the use of for loops or modulo operator
// Author: @StephenTrainor

#include <stdio.h>

int main(void) {
    double iterations;
    int fizz = 1;
    int buzz = 1;
    int i = 1;
    int temp1;
    int temp2;
    printf("Enter number to go up to: ");
    scanf("%lf", &iterations);
    do {
        fizz = 0;
        buzz = 0;
        temp1 = i;
        do {
            temp1 -= 3;
        }
        while (temp1 > 3);
        if (temp1 == 0 || temp1 == 3) {
            printf("Fizz");
            fizz++;
        }
        temp2 = i;
        do {
            temp2 -= 5;
        }
        while (temp2 > 5 || temp2 == 5);
        if (temp2 == 0) {
            printf("Buzz");
            buzz++;
        }
        if ((fizz == 0) && (buzz == 0)) {
            printf("%i", i);
        }
        printf("\n");
        i++;
    }
    while (i < iterations);
}
