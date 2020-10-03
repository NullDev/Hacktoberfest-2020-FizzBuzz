// A simple Fizzbuzz solution using do-while 
// Author : @JananiPN19 
// <Love coding/> :) 
 
#include<stdio.h> 

int main(){  
  print("0\n"); 
  int j=1; 
  do{ 
    if(j%15==0) printf("Fizzbuzz"); 
    else if(j%3==0) printf("Fizz"); 
    else if(j%5 == 0) printf("Buzz"); 
    else printf("%d",j); 
    printf("\n"); 
    j++; 
  }while(j <= 100); 
}
