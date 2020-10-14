#include <stdio.h>
#include <stdlib.h>

int isMul3(unsigned int n) {
    int odd = 0, even = 0;
    if (n == 0) return 1;
    if (n == 1) return 0;
    while (n) {
        if (n & 1)              // count n's odd bit
            odd++;
        n >>= 1;
        if (n & 1)              // count n's even bit
            even++;
        n >>= 1;
    }
    return (isMul3(abs(odd-even)));
}

int isMul5(unsigned int n) {
    int ret = 0;
    if (n == 0 || n == 5)       // return true if the input is 0 or 5
        return 1;
    if (n < 5)		            // return false if the input is not 0.
        return 0;
    while (n) {
        if (n & 1)	            // first bit, weighted is 1.
            ret++;
        n >>= 1;
        if (n & 1)		        // second bit, weighted is 2.
            ret+=2;
        n >>= 1;
        if (n & 1)		        // third bit, weighted is 4.
            ret+=4;	
        n >>= 1;
        if (n & 1)		        // fourth bit, weighted is 3.
            ret+=3;
        n >>= 1;
    }
    return(isMul5(abs(ret - 5)));
}

int main() {
    
    for (unsigned int i = 1; i <= 100; i++) {
        int t, f;
        if (t = isMul3(i))
            printf("Fizz");
        if (f = isMul5(i))
            printf("Buzz");
        if (!t && !f)
            printf("%d", i);
        printf("\n");
    }
    return 0;
}
