#include<stdio.h>
#include<string.h>
#include<math.h>
int func( int number)
{
    if (number%3==0 && number%5==0)
    {
        printf("fizz buzz ");
    }
    else if (number%5==0)
    {
        printf("buzz ");

    }
    else if (number%3==0)
    {
        printf("fizz  ");
    }
    else
    {
     printf("%d ",number);
    }
    return 0;
}
int main()
{
    int n,i;
    printf("enter no. of terms:");
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {
        func(i);
    }
    return 0;
}
