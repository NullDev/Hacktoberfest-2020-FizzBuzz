// Fizzbuzz using switch statement
// Author @NidhxGupta

#include <stdio.h>

int main(void)
{
    int i,n;

    for(i = 1 ; i < 101; i++)
    {
        if(i % 3 == 0 && i % 5 == 0)
        {
            n = 0; // If n is 0, Fizzbuzz
        }
        else if(i % 3 == 0)
        {
            n = 1; // If n is 1, Fizz
        }
        else if(i % 5 == 0)
        {
            n = 2; // If n is 2, Buzz
        }
        else
        {
            n = 3; // Integer
        }

        switch(n)
        {
            case 0: 
            {
                printf("Fizzbuzz\n");
                break;
            }
            case 1:
            {
                printf("Fizz\n");
                break;
            }
            case 2:
            {
                printf("Buzz\n");
                break;
            }
            case 3:
            {
                printf("%d\n",i);
                break;
            }
            default:
            {
                break;
            }
        }
    }

    return 0;
}