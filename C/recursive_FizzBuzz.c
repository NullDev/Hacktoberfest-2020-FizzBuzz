// FizzBuzz using recursion
// Author: @felipeMarajo

#include <stdio.h>

int FB(int number){
    if (number == 101){
        return 0;
    }else if (number%3 == 0 && number%5 == 0){
        printf("FizzBuzz \n");
    }else if (number%3 ==0){
        printf("Fizz \n");
    }else if (number%5 ==0){
        printf("Buzz \n");
    }else{
        printf("%d\n",number);
    }
    
    FB(number + 1);
}

int main(){
    FB(1);

    return 0;
}