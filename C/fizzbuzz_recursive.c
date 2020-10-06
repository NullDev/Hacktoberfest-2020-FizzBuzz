/*
 FizzBuzz using recursion in C. Takes 'n' input as command line parameter while running.
 Author: @evamy
*/

#include<stdio.h>
#include<stdlib.h>

void fizzbuzz(int current, int n) {
    if (current%3 == 0 && current%5 == 0) {
        printf("FizzBuzz\n");
    } else if (current%3 == 0) {
        printf("Fizz\n");
    } else if (current%5 == 0) {
        printf("Buzz\n");
    } else {
        printf("%d\n", current);
    }
    
    if (current < n) {
        return fizzbuzz(current+1, n);
    }
}

int main(int argc, char *argv[]) {
    if( argc > 2 ) {
       printf("Too many arguments supplied.\n");
       return -1;
    } else if (argc == 0) {
       printf("An argument expected.\n");
       return -1;
    }
    
    fizzbuzz(1, atoi(argv[1]));
    
    return 0;
}
