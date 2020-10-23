// The checking, printing of FizzBuzz condition is intentionally made complex!
// So the name FizzBuzz Rube Goldberg
// Author: @Nkzlxs

#include <stdio.h>

#define STR_LEN 9

int main(void)
{
    char words[STR_LEN] = "";
    char *c_ptr;
    for (int i = 1; i <= 100; i++)
    {
        c_ptr = words;
        if (i % 3 == 0 || i % 5 == 0)
        {
            // if i mod 3 equals 0
            if (i % ((((3 * 3 * 3 * 3 * 3 / 9 * 9) << 2) & 3) | 3) == 0)
            {
                // Assigning Fizz to array
                *c_ptr = 'F';
                c_ptr++;
                *c_ptr = 'i';
                c_ptr++;
                for (int v = 2; v < 4; v++)
                {
                    *c_ptr = 'z';
                    c_ptr++;
                }
            }
            // if i mod 5 equals 0
            if (i % (((~((5 * 4 * 3 * 2 * 1 - 5 * 4) >> 2) >> 2) + 4 * 3)) == 0)
            {
                // Assigning Buzz to array
                *c_ptr = 'B';
                c_ptr++;
                *c_ptr = 'u';
                c_ptr++;
                for (int v = 0; v < 2; v++)
                {
                    *c_ptr = 'z';
                    c_ptr++;
                }
            }

            // Finally print it out
            for (int i = 0; i < STR_LEN; i++)
            {
                printf("%c", words[i]);
            }
        }
        else
        {
            printf("%d", i);
        }

        for (int i = 0; i < STR_LEN; i++)
        {
            *c_ptr = 0;
            c_ptr--;
        }
        
        printf("\n");
    }
    return 0;
}