// A simple fizzbuzz program in C language by crypticani

#include<stdio.h>

int main()
{
    for(int i = 0; i<=100; i++)
    {
        if(i%3==0 && i%5==0)
        {
            printf("fizzbuzz\t");
        }
        else if (i%3 == 0)
        {
            printf("fizz\t");
        }
        else if (i%5 == 0)
        {
            printf("buzz\t");
        }
        else
        {
            printf("%d\t",i);
        }
    }
    return 0;
}
