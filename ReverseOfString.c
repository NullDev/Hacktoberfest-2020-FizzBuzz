#include <stdio.h>
#define MAX_SIZE 100 // Maximum string size

int main()
{
    char str[MAX_SIZE], reverse[MAX_SIZE];
    int i, strIndex, revIndex, len;

    /* Input string from user */
    printf("Enter any string: ");
    gets(str);

    /* Find length of string */
    i = 0;
    while(str[i] != '\0') i++;

    len = i;

    /* 
     * Store each character from end of original string 
     * to reverse string
     */
    revIndex = 0;
    strIndex = len - 1;
    while(strIndex >= 0)
    {
        reverse[revIndex] = str[strIndex];

        strIndex--;
        revIndex++;
    }
    reverse[revIndex] = '\0';

    printf("\nOriginal string = %s\n", str);
    printf("Reverse string = %s", reverse);

    return 0;
}