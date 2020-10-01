#include<bits/stdc++.h>
using namespace std;

void fizzbuzz(int n){
    for(int i=1;i<=n;i++){
        if (i%15 == 0)         
            printf ("FizzBuzz\t");     
        
        else if ((i%3) == 0)     
            printf("Fizz\t");                  
         
        else if ((i%5) == 0)                        
            printf("Buzz\t");                  
      
        else            
            printf("%d\t", i);  
    }
}
int main(){
    int n;
    cin>>n;
    fizzbuzz(n);
    return 0;
}