# optimised c code for fizz buzz
# author @aryamansinghk
#include <stdio.h>

int main()
{
    int i,l1,l2;
    printf("enter range of fizz buzz calculation");
    scanf("%d %d",&l1,&l2);
    for(i=l1;i<=l2;i++)
    {
        if(i%3==0)
        {
            if(i%5==0)
                printf("FizzBuzz\n");
            else
                printf("Fizz\n");
        }
        else
            printf("Buzz\n");
    }
    return 0;
}
