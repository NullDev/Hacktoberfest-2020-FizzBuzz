// tried to do it in simplest possible way
// Author: @brigadierpratap

#include <stdio.h>
void fizzbuzz(){
    for(int i=1;i<101;i++){
        if(i%3==0){
            if(i%5==0){
                printf("FizzBuzz\n");
            }
            else{
                printf("Fizz\n");
            }
        }else if(i%5==0){
            printf("Buzz\n");
        }else printf("%d\n",i);
    }
}
int main()
{
    fizzbuzz();
}
