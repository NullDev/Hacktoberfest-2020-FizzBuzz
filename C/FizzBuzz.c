//C code to implement FizzBuzz
//Author @GhostUser

#include <stdio.h>

int main(){
    for(int FizzBuzz=0; FizzBuzz<101;FizzBuzz++){
        if (FizzBuzz%3==0 && FizzBuzz%5==0){
            printf("FizzBuzz\n");
        }
        else if (FizzBuzz%3==0){
            printf("Fizz\n");
        }
        else if(FizzBuzz%5==0){
            printf("Buzz\n");
        }
        else{
            printf("%d\n", FizzBuzz);
        }
    }
    return 0;
}