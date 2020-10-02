#include<stdio.h>
#include<conio.h>
void main(){
    int a=0;
    int b=1;
    int new_term;
    clrscr();
    for(i=1;i<=6;i++)
    {
        printf("%d \n",a);
        new_term=a+b;
        a=b;
        b=new_term;
    }
    getch();
}