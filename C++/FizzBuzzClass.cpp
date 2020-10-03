// Author @aryamansinghk
// Used classes and objects in order to compute fizz and buzz upto n numbers.
#include <stdio.h>
class fizzbuzz
{
    public:
    int input()
    {   
        int n;
        printf("enter number to which you wanna calculate fizzBuzz \t");
        scanf("%d",&n);
        return n;
    }
    int fizzBuzz(int x)
    {
        if(x%3==0 && x%5==0)
            return 1;
        else
            return 0;
    }
    int fizz(int x)
    {
        if(x%3==0)
            return 1;
        else
            return 0;
    }
    int buzz(int x)
    {
        if (x%5==0)
            return 1;
        else
            return 0;
    }
    
};
int main()
{
    fizzbuzz F;
    int n = F.input();
    int i;
    for(i=1;i<=n;i++)
    {
        if(F.fizzBuzz(i))
            printf("FizzBuzz \n");
        else if(F.fizz(i))
            printf("Fizz \n");
        else if(F.buzz(i))
            printf("Buzz \n");
        else
            printf("%d \n",i);
    }
    return 0;
}
