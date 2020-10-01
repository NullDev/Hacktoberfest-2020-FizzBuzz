#include<stdio.h>
#include<math.h>
#include<stdlib.h>

void accept(int a[20], int n) ;
void display(int a[20], int n) ;
void quicksort(int a[20], int low, int high) ;
int partition(int a[20], int low, int high) ;

void main()
{
    int a[20], n, choice ;
    do
    {
        printf("\n\n MAIN MENU \n1)Accept:-  \n2)Display:-  \n3)Apply Quick Sort:-  \n4)Exit  \nEnter your choice:-  ") ;
        scanf("%d", &choice) ;
        switch(choice)
        {
            case 1 :
                printf("\nEnter the number of elements:-  ") ;
                scanf("%d", &n) ;
                printf("\nEnter the element of array ::=  ") ;
                accept(a, n) ;
                break ;


            case 2 :
                printf("\nArray Elelment:-  ") ;
                display(a, n) ;
                break ;


            case 3 :
                quicksort(a, 0, n-1) ;
                printf("\nSorted Array is :-  ") ;
                display(a, n) ;
                break ;
        }
    }while(choice!=4) ;
}


void accept(int a[20], int n)
{
    for(int i=0 ; i<n ; i++)
    {
        printf("\nEnter the number of [%d]:- ", i) ;
        scanf("%d", &a[i]) ;
    }
}


void display(int a[20], int n)
{
    for(int i=0 ; i<n ; i++)
    {
        printf("\t%d", a[i]) ;
    }
}


void quicksort(int a[20], int low, int high)
{
    int m ;
    if(low < high)
    {
        m = partition(a, low, high) ;
        quicksort(a, low, m-1) ;
        quicksort(a, m+1, high) ;
    }
}


int partition(int a[20], int low, int high)
{
    int temp, i, j ;
    int pivot = a[low] ;
    i=low+1 ;
    j=high ;

    while(i <= j)
    {
       while(pivot > a[i])
       {
           i++ ;
       }

       while(a[j] > pivot)
       {
           j-- ;
       }

       if(j > i)
       {
           temp = a[i] ;
           a[i] = a[j] ;
           a[j] = temp ;
       }
    }
    temp = a[low] ;
    a[low] = a[j] ;
    a[j] = temp ;

    printf("\n Partition at:- %d\t", j) ;

    for(int i=0 ; i<=high ; i++)
    {
        printf("%d", a[i]) ;
    }
    return j ;
}








